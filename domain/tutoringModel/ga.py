import math
import numpy as np
from sklearn.metrics import pairwise_distances_argmin
# from domain.tutoringModel import model
from domain.tutoringModel import utils
import errors as err


class GaAlgorithmus(object):
    """GaAlgorithmus"""
    def __init__(self,                
                 learning_style=None,
                 learning_elements=None,
                 ):

        self.pop_size = 80
        self.cross_rate = 0.9
        self.mutate_rate = 0.3
        self.n_generation = 100
        self.best_population = None
        self.le_coordinate = None
        self.learning_elements = learning_elements
        self.le_size = None
        self.population = None
        
        if learning_elements is not None:
            self.learning_elements = utils.get_list_learning_element(
                learning_elements)
            self.le_size = len(self.learning_elements)

    def create_random_population(self, dict_coordinates) -> None:
        """function for the calculation of the score.
           position a also Initialise some populations
           with Clustering if this is possible.
           param dict_coordinates  """
        self.le_coordinate = np.array(
            [dict_coordinates[key]for key in dict_coordinates])
        self.le_coordinate.reshape((len(dict_coordinates), 4))

        positions = np.arange(1, self.le_size)
        self.population = np.vstack(
            [np.random.permutation(positions)
             for _ in range(self.pop_size)])

        is_not_none = False
        is_not_none, labels = self.find_cluster_between_le(
            self.le_coordinate, n_cluster=3, rseed=2)
        if is_not_none:
            daten = self.get_clustering_order(positions, labels)
            self.population[0:-2, :] = daten

    def valide_population(self):
        """Function to add validation:
           First Learning Element is fixed in the Learning path."""
        new_pop = np.zeros((self.pop_size,
                            self.le_size),
                           dtype=int)
        new_pop[:, 0] = 0
        # new_pop[:, self.le_size -1] = self.le_size -1
        new_pop[:, 1:self.le_size] = self.population.copy()
        return new_pop

    def get_lines_paths(self, new_pop):
        """This function extract all the positions X,Y,Z,K.
        in the space of the generated trajectories"""
        line_x = np.empty_like(new_pop, dtype=np.float64)
        line_y = np.empty_like(new_pop, dtype=np.float64)
        line_z = np.empty_like(new_pop, dtype=np.float64)
        line_k = np.empty_like(new_pop, dtype=np.float64)
        # total_distance = np.empty((line_x.shape[0],),
        # dtype=np.float64)
        for i, j in enumerate(new_pop):
            le_coord = self.le_coordinate[j]
            line_x[i, :] = le_coord[:, 0]
            line_y[i, :] = le_coord[:, 1]
            line_z[i, :] = le_coord[:, 2]
            line_k[i, :] = le_coord[:, 3]
        return line_x, line_y, line_z, line_k

    def get_fitness(self, line_x, line_y, line_z, line_k):
        """Funcion para Berechnung der Fitnessnote."""
        # a score is evaluated for each individual, which is
        # calculated using the fitness function: dtype=np.float64)
        total_sum = (np.square(np.diff(line_x))
                     + np.square(np.diff(line_y))
                     + np.square(np.diff(line_z))
                     + np.square(np.diff(line_k)))
        fitness = np.sqrt(np.sum(total_sum, 1))
        return fitness

    def crossover(self, parent, pop):
        """function for the calculation 
        of crossovers between each individual."""
        # two parents are randomly
        # selected from the population, to pass on a part
        # of their solution to their child.  """

        if np.random.rand() < self.cross_rate:
            samples = 2
            i_ = np.random.randint(0, samples, size=1)
            # choose crossover learning elements
            temp = self.le_size - 1
            cross_points = np.random.randint(0, 2, temp).astype(bool)
            keep_le = parent[~cross_points]
            swap_le = pop[i_, np.isin(pop[i_].ravel(), keep_le, invert=True)]
            parent = np.concatenate((keep_le, swap_le))
        return parent

    def mutate(self, child):
        """funcion fo"""
        # To prevent all offspring of a new generation
        # from having the same approximation, a percentage
        # probability is set at which an offspring will receive
        # a mutation. In this case, two points within the pathway
        # are exchanged. This creates a new pathway that
        # may not appear in the previous generation """
        temp = self.le_size - 2
        for point in range(temp):
            if np.random.rand() < self.mutate_rate:
                swap_point = np.random.randint(0, int(temp))
                swap_a, swap_b = child[point], child[swap_point]
                child[point], child[swap_point] = swap_b, swap_a
        return child

    def evolve(self, fitness, best_sample) -> None:
        """In the selection phase, after knowing
        the aptitude of each individual, those that will be selected
        of each individual, those that are
        most suitable to evolve will be selected."""
        best_samples = 7
        if self.pop_size > 50:
            self.population[20:-3, :] = best_sample

        idx = np.argsort(fitness)
        population = self.population[idx]

        pop_copy = population.copy()

        for parent in population:
            child = self.crossover(parent, pop_copy)
            child = self.mutate(child)
            parent[:] = child

        self.population[best_samples:] = population[best_samples:].copy()

    def calculate_distance(self, best_population) -> float:
        """In the selection phase, after knowing
        the aptitude of each individual, those that will be selected
        of each individual, those that are most suitable
        to evolve will be selected."""
        sume = 0
        le_coordinate = self.le_coordinate
        # index = np.append(best_population, self.le_size-1)
        index = best_population
        index = np.append(0, index)
        if (len(index) > 10):
            le_coordinate = self.le_coordinate[index]

        for i in range(len(index)-1):
            temp1 = le_coordinate[i]
            temp2 = le_coordinate[i+1]
            sume = sume + math.dist(temp1, temp2)

        euclidean_distance = round(sume, 2)
        return euclidean_distance

    def find_cluster_between_le(self, daten, n_cluster=3, rseed=2) -> bool:
        """ this function calculates the clustering """
        labels = []
        if len(daten) <= 0:
            return False, labels
        rng = np.random.RandomState(rseed)
        i = rng.permutation(daten.shape[0])[:n_cluster]
        centers = daten[i]
        new_centers = np.unique(centers, axis=0)
        if len(new_centers) < n_cluster:
            return False, labels

        while (True):
            labels = pairwise_distances_argmin(daten, centers)
            mean_cluster = [daten[labels == i].mean(0)
                            for i in range(n_cluster)]
            new_centers = np.array(mean_cluster)

            if (np.all(centers == new_centers)):
                break
            else:
                centers = new_centers

        return True, labels

    def get_clustering_order(self, daten, labels):
        """this function organises the clustering."""
        labels = labels[1:]
        positions = np.arange(1, self.le_size)
        label_0 = positions[labels == 0]
        label_1 = positions[labels == 1]
        label_2 = positions[labels == 2]

        daten = np.concatenate((label_2, label_0), axis=None)
        daten = np.concatenate((daten, label_1), axis=None)

        daten = np.concatenate((0, daten), axis=None)
        # ga_path = np.array(self.learning_elements)
        print(daten)
        # print(ga_path)
        # self.daten_compare = daten
        return daten

    def calculate_learning_path(self, learning_style):
        """this function calculates the learning path."""
        best_total_score = 300
        le_coordinate = utils.get_coordinates(
            learning_style, self.learning_elements)

        self.create_random_population(le_coordinate)

        for i in range(self.n_generation):

            new_pop = self.valide_population()
            lx, ly, lz, lk = self.get_lines_paths(new_pop)
            fitness = self.get_fitness(lx, ly, lz, lk)

            # sort population
            best_index = np.argsort(fitness)
            fitness = fitness[best_index]
            best_score = fitness[0]

            # update population
            new_pop = self.population[best_index].copy()
            self.population = new_pop.copy()
            best_sample = new_pop[0]

            if best_score < best_total_score:

                best_total_score = best_score
                self.best_population = best_sample

            # evolution
            self.evolve(fitness, best_sample)

        # euclidean_distance = self.calculate_distance(best_sample)

        ga_path = np.array(self.learning_elements)
        population = self.valide_population()
        idx = population[0]
        result_ga_lp = ga_path[idx]

        learning_path = self.get_learning_path_as_str(result_ga_lp)

        return learning_path

    def get_learning_path_as_str(self, result_ga):

        str_learning_path = ""
        contain_le = False
        for ele in result_ga:
            str_learning_path = str_learning_path + ele + ', '
            contain_le = True

        if contain_le:
            str_learning_path = str_learning_path[:-2]

        return str_learning_path

    def get_learning_path(self, input_learning_style=None,
                          input_learning_element=None):
        result_ga = []
        # time1 = time.time()

        if input_learning_style is not None:
            learning_style = utils.get_learning_style(input_learning_style)

        if len(learning_style) != 4:
            raise err.WrongLearningStyleNumberError()

        if utils.check_learning_style(learning_style):
            raise err.WrongLearningStyleDimensionError()

        if utils.check_name_learning_style(learning_style):
            raise err.WrongLearningStyleDimensionError()

        if input_learning_element is not None:
            self.learning_elements = utils.get_list_learning_element(
                input_learning_element)
            self.le_size = len(self.learning_elements)
        else:
            raise err.WrongLearningStyleDimensionError()

        result_ga = self.calculate_learning_path(input_learning_style)

        # time2 = time.time()
        # time_sec = time2-time1
        # print("Time_sec: ", time_sec)
        print("\nResult_GA_Learning path: ", result_ga)
        # print("\n\n")

        return result_ga
