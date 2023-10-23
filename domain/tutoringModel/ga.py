import math

import numpy as np

import errors as err
from domain.tutoringModel import utils


class Genetische_Algorithm:
    """Genetische Algorithmus  sdfasdfs"""

    def __init__(
        self,
        learning_style=None,
        learning_elements=None,
    ):
        self.learning_elements = learning_elements
        self.best_population = None
        self.le_coordinate = None
        self.n_generation = 100
        self.population = None
        self.le_size = None
        self.mutate_rate = 0.3
        self.cross_rate = 0.9
        self.pop_size = 80

    def create_random_population(self, dict_coordinates) -> None:
        """function for the calculation of the score.
        position a also Initialise some populations
        with Clustering if this is possible.
        param dict_coordinates"""
        self.le_coordinate = np.array(
            [dict_coordinates[key] for key in dict_coordinates]
        )
        self.le_coordinate.reshape((len(dict_coordinates), 4))

        positions = np.arange(1, self.le_size)
        self.population = np.vstack(
            [np.random.permutation(positions) for _ in range(self.pop_size)]
        )

    def valide_population(self):
        """Function to add validation:
        First Learning Element is fixed
        in the Learning path."""

        new_pop = np.zeros((self.pop_size, self.le_size), dtype=int)
        new_pop[:, 0] = 0

        new_pop[:, 1 : self.le_size] = self.population.copy()
        return new_pop

    def get_lines_paths(self, new_pop):
        """This function extract all the positions X,Y,Z,K.
        in the space of the generated trajectories"""
        line_x = np.empty_like(new_pop, dtype=np.float64)
        line_y = np.empty_like(new_pop, dtype=np.float64)
        line_z = np.empty_like(new_pop, dtype=np.float64)
        line_k = np.empty_like(new_pop, dtype=np.float64)

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
        total_sum = (
            np.square(np.diff(line_x))
            + np.square(np.diff(line_y))
            + np.square(np.diff(line_z))
            + np.square(np.diff(line_k))
        )
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
        # may not appear in the previous generation
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

        index = best_population
        index = np.append(0, index)
        if len(index) > 10:
            le_coordinate = self.le_coordinate[index]

        for i in range(len(index) - 1):
            temp1 = le_coordinate[i]
            temp2 = le_coordinate[i + 1]
            sume = sume + math.dist(temp1, temp2)

        euclidean_distance = round(sume, 2)
        return euclidean_distance

    def calculate_learning_path_ga(self, learning_style):
        """this function calculates the learning path."""
        best_total_score = 300
        le_coordinate = utils.get_coordinates(learning_style, self.learning_elements)

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
            # print("generation:", i)
            if best_score < best_total_score and i < self.n_generation:
                best_total_score = best_score
                self.best_population = best_sample

            # evolution
            self.evolve(fitness, best_sample)

        ga_path = np.array(self.learning_elements)
        population = self.valide_population()
        idx = population[0]
        result_ga_lp = ga_path[idx]

        # convert to string
        learning_path = self.get_learning_path_as_str(result_ga_lp)

        return learning_path

    def get_learning_path_as_str(self, result_ga):
        """.."""
        str_learning_path = ""
        contain_le = False
        for ele in result_ga:
            str_learning_path = str_learning_path + ele + ", "
            contain_le = True

        if contain_le:
            str_learning_path = str_learning_path[:-2]

        return str_learning_path

    def get_learning_style(self, learning_style):
        """..."""

        new_learning_style = {}
        str_processing = learning_style.get("processing_dimension")
        value_processing = learning_style.get("processing_value")
        new_learning_style[str_processing] = value_processing

        str_perception = learning_style.get("perception_dimension")
        value_perception = learning_style.get("perception_value")
        new_learning_style[str_perception] = value_perception

        str_input = learning_style.get("input_dimension")
        value_input = learning_style.get("input_value")
        new_learning_style[str_input] = value_input

        str_understanding = learning_style.get("understanding_dimension")
        value_understanding = learning_style.get("understanding_value")
        new_learning_style[str_understanding] = value_understanding

        for key, value in dict(new_learning_style).items():
            if value is None:
                del new_learning_style[key]

        return new_learning_style

    def check_learning_style(self, input_learning_style):
        """check_learning_style"""
        is_correct = False
        for iterator in input_learning_style:
            if input_learning_style.get(iterator):
                dimension_number = input_learning_style.get(iterator)
                if dimension_number < 0 or dimension_number > 11:
                    is_correct = True
                    break

        return is_correct

    def check_name_learning_style(self, input_learning_style):
        """this ist no necesary"""

        list_is_correct = []
        for iterator in input_learning_style:
            condition1 = iterator == "act" or iterator == "ref"
            condition2 = iterator == "sns" or iterator == "int"
            condition3 = iterator == "vis" or iterator == "vrb"
            condition4 = iterator == "seq" or iterator == "glo"
            if condition1 or condition2 or condition3 or condition4:
                list_is_correct.append(True)
        temp = [True, True, True, True]
        if list_is_correct != temp:
            return True

        return False

    def get_learning_element(self, learning_elements):
        classification_learning_element = []
        lz_is_present = False
        lz_element = ""

        for le in learning_elements:
            if le["classification"] == "KÜ":
                classification_learning_element.insert(0, le["classification"])
            elif le["classification"] == "LZ":
                lz_is_present = True
                lz_element = le["classification"]
            else:
                classification_learning_element.append(le["classification"])

        if lz_is_present:
            classification_learning_element.append(lz_element)
        print("learning elements", classification_learning_element)
        return classification_learning_element

    def get_learning_path(self, input_learning_style=None, input_learning_element=None):
        """.."""
        result_ga = []
        if input_learning_style is not None:
            learning_style = self.get_learning_style(input_learning_style)

        if len(learning_style) != 4:
            raise err.WrongLearningStyleNumberError()

        if self.check_learning_style(learning_style):
            raise err.WrongLearningStyleDimensionError()

        if self.check_name_learning_style(learning_style):
            raise err.WrongLearningStyleDimensionError()

        # esto hay que modificarlo no sabemos si viene Vacio
        if input_learning_element is not None:
            # added more learning elementen
            # input_learning_element = self.add_Learning_element(
            # input_learning_element)
            self.learning_elements = self.get_learning_element(input_learning_element)
            self.le_size = len(self.learning_elements)
        else:
            raise err.WrongLearningStyleDimensionError()

        result_ga = self.calculate_learning_path_ga(input_learning_style)
        print("Learning stylw", input_learning_style)
        print("\nResult input_learning_element: ", input_learning_style)
        return result_ga
