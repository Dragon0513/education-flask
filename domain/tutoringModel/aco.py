from itertools import chain
from typing import Any, List, Tuple
import time
import random
import numpy as np
from domain.tutoringModel import utils


class AntColonySolver:
    def __init__(self):
        self.cost_fn = utils.distance
        self.time = 0
        self.min_time = 0
        self.timeout = 0
        self.stop_factor = 2
        self.min_round_trips = 10
        self.max_round_trips = 0
        self.min_ants = 0
        self.max_ants = 0

        self.ant_count = 64
        self.ant_speed = 1

        self.distance_power = 5
        self.pheromone_power = 1.5
        self.decay_power = 0
        self.reward_power = 0
        self.best_path_smell = 5
        self.start_smell = 1

        self._initalized = False

        if self.min_round_trips and self.max_round_trips:
            self.min_round_trips = min(
                self.min_round_trips, self.max_round_trips)
        if self.min_ants and self.max_ants:
            self.min_ants = min(self.min_ants, self.max_ants)

    def solve_initialize(
            self,
            problem_path: List[Any],
    ) -> None:
        # Cache of distances between nodes
        self.distances = {
            source: {
                dest: self.cost_fn(source, dest)
                for dest in problem_path
            }
            for source in problem_path
        }

        # Cache of distance costs between nodes
        # - division in a tight loop is expensive
        self.distance_cost = {
            source: {
                dest: 1 / (1 + self.distances[source]
                           [dest]) ** self.distance_power
                for dest in problem_path
            }
            for source in problem_path
        }

        # This stores the pheromone trail that slowly builds up
        self.pheromones = {
            source: {
                # Encourage the ants to start exploring
                # in all directions and furthest nodes
                dest: self.start_smell
                for dest in problem_path
            }
            for source in problem_path
        }

        # Sanitise input parameters
        if self.ant_count <= 0:
            self.ant_count = len(problem_path)
        if self.ant_speed <= 0:
            self.ant_speed = np.median(
                list(chain(*[d.values()
                             for d in self.distances.values()]))) // 5
        self.ant_speed = int(max(1, self.ant_speed))

        # Heuristic Exports
        self.ants_used = 0
        self.epochs_used = 0
        self.round_trips = 0
        self._initalized = True

    def solve(self,
              problem_path: List[Any],
              restart=False,
              ) -> List[Tuple[int, int]]:

        if restart or not self._initalized:
            self.solve_initialize(problem_path)

        # Here come the ants!
        ants = {
            "distance":
            np.zeros((self.ant_count,)).astype('int32'),
            "path":
            [[problem_path[0]] for _ in range(self.ant_count)],
            "remaining":
                [set(problem_path[1:-1]) for _ in range(self.ant_count)],
            "end":
            problem_path[-1],
            "path_cost":
            np.zeros((self.ant_count,)).astype('int32'),
            "round_trips":
            np.zeros((self.ant_count,)).astype('int32'),
        }

        best_path = None
        best_path_cost = np.inf
        best_epochs = []
        epoch = 0
        time_start = time.perf_counter()
        while True:
            epoch += 1

            # Vectorized walking of ants
            # Small optimization here, testing against
            # `> self.ant_speed` rather than `> 0`
            # avoids computing ants_arriving in the main part
            # of this tight loop
            ants_travelling = (ants['distance'] > self.ant_speed)
            ants['distance'][ants_travelling] -= self.ant_speed
            if all(ants_travelling):
                continue  # skip termination checks until the next ant arrives

            # Vectorized checking of ants arriving
            ants_arriving = np.invert(ants_travelling)
            ants_arriving_index = np.where(ants_arriving)[0]
            for i in ants_arriving_index:
                ants, best_path, best_path_cost, best_epochs =\
                    self.ants_arriving(
                        ants,
                        i,
                        epoch,
                        problem_path,
                        best_path,
                        best_path_cost,
                        best_epochs)

            if self.loop_termination(best_epochs, time_start, epoch):
                break
            else:
                continue

        # We have (hopefully) found a near-optimal path,
        # report back to the Queen
        self.epochs_used = epoch
        self.round_trips = np.max(ants["round_trips"])
        return best_path

    def next_node(self, ants, index):
        this_node = ants['path'][index][-1]

        weights = []
        weights_sum = 0
        if not ants['remaining'][index]:
            # ants return home
            return ants['path'][index][0]
        for next_node in ants['remaining'][index]:
            if next_node == this_node:
                continue
            reward = (
                self.pheromones[this_node][next_node] ** self.pheromone_power
                # Prefer shorter paths
                * self.distance_cost[this_node][next_node]
            )
            weights.append((reward, next_node))
            weights_sum += reward

        # Pick a random path in proportion to the weight of the pheromone
        rand = random.random() * weights_sum
        for (weight, next_node) in weights:
            if rand > weight:
                rand -= weight
            else:
                break
        return next_node

    def ants_arriving(self,
                      ants,
                      i,
                      epoch,
                      problem_path,
                      best_path,
                      best_path_cost,
                      best_epochs):
        # ant has arrived at next_node
        this_node = ants['path'][i][-1]
        next_node = self.next_node(ants, i)
        ants['distance'][i] = self.distances[this_node][next_node]
        ants['remaining'][i] = ants['remaining'][i] - {this_node}
        ants['path_cost'][i] = ants['path_cost'][i] + \
            ants['distance'][i]
        ants['path'][i].append(next_node)

        # ant has returned home to the colony
        # and ants['end'] == ants['path'][i][-1]:
        if not ants['remaining'][i]:
            ants['path'][i].pop(-1)
            ants['path'][i].append(ants['end'])
            self.ants_used += 1
            self.round_trips = max(
                self.round_trips, ants["round_trips"][i] + 1)

            # We have found a new best path - inform the Queen
            was_best_path = False
            if ants['path_cost'][i] < best_path_cost:
                was_best_path = True
                best_path_cost = ants['path_cost'][i]
                best_path = ants['path'][i]
                best_epochs += [epoch]

            # leave pheromone trail
            # doing this only after ants arrive home improves
            # initial exploration
            #  * self.round_trips has the effect
            #    of decaying old pheromone trails
            # ** self.reward_power =
            #       -3 has the effect of encouraging ants to explore longer
            #       routes in combination with doubling pheromone for best_path
            reward = 1
            if self.reward_power:
                reward *= ((best_path_cost /
                            ants['path_cost'][i]) ** self.reward_power)
            if self.decay_power:
                reward *= (self.round_trips ** self.decay_power)
            for path_index in range(len(ants['path'][i]) - 1):
                this_node = ants['path'][i][path_index]
                next_node = ants['path'][i][path_index+1]
                self.pheromones[this_node][next_node] += reward
                self.pheromones[next_node][this_node] += reward
                if was_best_path:
                    # Queen orders to double the number
                    # of ants following this new best path
                    self.pheromones[this_node][next_node]\
                        *= self.best_path_smell
                    self.pheromones[next_node][this_node]\
                        *= self.best_path_smell

            # reset ant
            ants["distance"][i] = 0
            ants["path"][i] = [problem_path[0]]
            ants["remaining"][i] = set(problem_path[1:-1])
            ants["end"] = problem_path[-1]
            ants["path_cost"][i] = 0
            ants["round_trips"][i] += 1

        return ants, best_path, best_path_cost, best_epochs

    def loop_termination(self,
                         best_epochs,
                         time_start,
                         epoch):
        # Do we terminate?

        # Always wait for at least 1 solutions
        # (note: 2+ solutions are not guaranteed)
        if not len(best_epochs):
            return False

        # Timer takes priority over other constraints
        if self.time or self.min_time or self.timeout:
            return self.loop_termination_time(time_start)

        # First epoch only has start smell - question:
        # how many epochs are required for a reasonable result?
        if self.min_round_trips and self.round_trips < self.min_round_trips:
            return False
        if self.max_round_trips and self.round_trips >= self.max_round_trips:
            return True

        # This factor is most closely tied to computational power
        if self.min_ants and self.ants_used < self.min_ants:
            return False
        if self.max_ants and self.ants_used >= self.max_ants:
            return True

        # Lets keep redoubling our efforts until we can't find anything more
        if self.stop_factor and epoch > (best_epochs[-1] * self.stop_factor):
            return True

    def loop_termination_time(self, time_start):
        clock = time.perf_counter() - time_start
        if self.time:
            if clock > self.time:
                return True
            else:
                return False
        if self.min_time and clock < self.min_time:
            return False
        if self.timeout and clock > self.timeout:
            return True
