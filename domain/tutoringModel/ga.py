from sklearn.metrics import pairwise_distances_argmin
from domain.tutoringModel import util
from domain.tutoringModel import model
from datetime import datetime
import errors as err
import numpy as np
import math
import time


class GA_Algorithmus(object):

    learning_elements = ["KÜ", "LK", "ZF", "RQ", "SE",
                         "FO", "ZL", "AN", "ÜB", "BE", "AB", "LZ"]
    best_population = None
    n_generation = 80
    mutate_rate = 0.2
    cross_rate = 0.8
    pop_size = 80

    def __init__(self,
                 student_id=0,
                 learning_path=None,
                 learning_style={"REF": 1, "SNS": 3, "VIS": 5, "SEQ": 5},
                 learning_elements=None,
                 id=None):
        if id is None:
            self.id = datetime.timestamp(datetime.now())
        else:
            self.id = id
        
        if(learning_elements is not None):

            self.learning_elements = learning_elements

        self.le_size = len(self.learning_elements)

        if learning_path is None:

            self.learning_path = None  # self.get_learning_path(learning_style)
        else:
            self.learning_path = learning_path

        self.student_id = student_id

    def create_random_population(self):

        # genereate random position of population
        positions = np.arange(1, self.le_size)
        self.population = np.vstack(
            [np.random.permutation(positions)
             for _ in range(self.pop_size)])

        if (self.pop_size > 30):
            labels = self.find_cluster(
                self.le_coordinate,
                n_cluster=3,
                rseed=2)
            daten = self.get_daten_cluster(positions, labels)
            self.population[0:self.pop_size-1, :] = daten

    def valide_population(self):

        # The first and the last LE are fixed in the LPath
        new_pop = np.zeros((self.pop_size,
                            self.le_size),
                           dtype=int)
        new_pop[:, 0] = 0
        #new_pop[:, self.le_size -1] = self.le_size -1
        new_pop[:, 1:self.le_size] = self.population.copy()
        return new_pop

    def get_lines_paths(self, new_pop):

        line_x = np.empty_like(new_pop, dtype=np.float64)
        line_y = np.empty_like(new_pop, dtype=np.float64)
        line_z = np.empty_like(new_pop, dtype=np.float64)
        line_k = np.empty_like(new_pop, dtype=np.float64)
        total_distance = np.empty((line_x.shape[0],), dtype=np.float64)

        for i, d in enumerate(new_pop):
            LE_coord = self.le_coordinate[d]
            line_x[i, :] = LE_coord[:, 0]
            line_y[i, :] = LE_coord[:, 1]
            line_z[i, :] = LE_coord[:, 2]
            line_k[i, :] = LE_coord[:, 3]
        return line_x, line_y, line_z, line_k

    def get_fitness(self, line_x, line_y, line_z, line_k):

        re = list(zip(line_x, line_y, line_z, line_k))
        total_distance = np.empty((line_x.shape[0],), dtype=np.float64)
        total_sum = (np.square(np.diff(line_x)) +
                     np.square(np.diff(line_y)) +
                     np.square(np.diff(line_z)) +
                     np.square(np.diff(line_k)))
        fitness = np.sqrt(np.sum(total_sum, 1))
        return fitness

    def set_best_sample(self, sample):
        if (self.pop_size > 50):
            temp = self.pop_size-3
            self.population[20:temp, :] = sample

    def sort_population(self, fitness):

        idx = np.argsort(fitness)
        return self.population[idx]

    def crossover(self, parent, pop):

        if np.random.rand() < self.cross_rate:

            samples = 2
            i_ = np.random.randint(0, samples, size=1)
            # choose crossover learning elements
            temp = (self.le_size - 1)
            cross_points = np.random.randint(0, 2, temp).astype(bool)
            # choose the crossover learning element
            keep_LE = parent[~cross_points]  # find the LE number
            swap_LE = pop[i_, np.isin(pop[i_].ravel(), keep_LE, invert=True)]
            parent[:] = np.concatenate((keep_LE, swap_LE))
        return parent

    def mutate(self, child):

        child_copy = child.copy()
        temp = (self.le_size - 2)
        for point in range(temp):
            if np.random.rand() < self.mutate_rate:
                swap_point = np.random.randint(0, int(temp))
                swapA, swapB = child[point], child[swap_point]
                child[point], child[swap_point] = swapB, swapA
        return child

    def evolve(self, fitness, best_sample):

        self.set_best_sample(best_sample)
        population = self.sort_population(fitness)
        pop_copy = population.copy()

        for parent in population:
            child = self.crossover(parent, pop_copy)
            child = self.mutate(child)
            parent[:] = child

        best_samples = 7
        self.population[best_samples:] = population[best_samples:].copy()

    def calculate_distance(self, best_population):

        sume = 0
        LE_coordinate = self.le_coordinate
        #index = np.append(best_population, self.le_size-1)
        index = best_population
        index = np.append(0, index)
        if (len(index) > 10):
            LE_coordinate = self.le_coordinate[index]

        for i in range(len(index)-1):
            temp1 = LE_coordinate[i]
            temp2 = LE_coordinate[i+1]
            sume = sume + math.dist(temp1, temp2)

        euclidean_distance = round(sume, 2)
        return euclidean_distance

    def find_cluster(self, coordinates, n_cluster=3, rseed=2):

        daten = coordinates
        rng = np.random.RandomState(rseed)
        i = rng.permutation(daten.shape[0])[:n_cluster]
        centers = daten[i]
        while (True):
            labels = pairwise_distances_argmin(daten, centers)
            mean_cluster = [daten[labels == i].mean(0)
                            for i in range(n_cluster)]
            new_centers = np.array(mean_cluster)

            if (np.all(centers == new_centers)):
                break
            else:
                centers = new_centers

        return labels

    def get_daten_cluster(self, daten, labels):

        labels = labels[1:len(labels)]

        temp = self.le_size
        positions = np.arange(1, temp)
        label_0 = positions[labels == 0]
        label_1 = positions[labels == 1]
        label_2 = positions[labels == 2]
        daten = np.concatenate((label_2, label_1), axis=None)
        daten = np.concatenate((daten, label_0), axis=None)

        return daten

    def calculate_learning_path(self, learning_style):

        euclidean_distance = 0
        best_total_score = 300
        self.le_coordinate = util.get_coordinate(
            learning_style, self.learning_elements)
        self.create_random_population()

        for generatiion in range(self.n_generation):

            new_pop = self.valide_population()
            lx, ly, lz, lk = self.get_lines_paths(new_pop)
            fitness = self.get_fitness(lx, ly, lz, lk)

            #sort population
            best_index = np.argsort(fitness)
            fitness = fitness[best_index]
            best_score = fitness[0]

            # update population
            new_pop = self.population[best_index].copy()
            self.population = new_pop.copy()
            best_sample = new_pop[0]

            if (best_score < best_total_score):

                best_total_score = best_score
                self.best_population = best_sample

            # evolution
            self.evolve(fitness, best_sample)

        euclidean_distance = self.calculate_distance(best_sample)
        #print("euclidean_distance:", euclidean_distance)

    def get_learning_path(self, input_learning_style={"ACT": 1, "SNS": 7,
                                                      "VIS": 5, "GLO": 1},
                          dict_Learning_element=None):
        time1 = time.time()

        if (len(input_learning_style) != 4):
            raise err.WrongLearningStyleNumberError()

        if util.check_learning_style(input_learning_style):
            raise err.WrongLearningStyleDimensionError()

        if util.check_name_learning_style(input_learning_style):
            raise err.WrongLearningStyleDimensionError()

        learning_path = []
        self.calculate_learning_path(input_learning_style)

        elements = np.array(self.learning_elements)
        population = self.valide_population()
        idx = population[0]
        sort_learning_path = elements[idx]

        for i in range(len(sort_learning_path)):
            value = sort_learning_path[i]
            #learning_path[str(i)] = value
            learning_path.append(value)

        time2 = time.time()
        time_sec = time2-time1

        Learning_Path_id = self.id
        List_LPLE = util.get_list_LPLE(learning_path,
                                       dict_Learning_element,
                                       Learning_Path_id)

        print(Learning_Path_id)
        print('function took {:.4f} seconds'.format(time_sec))
        return learning_path, List_LPLE
