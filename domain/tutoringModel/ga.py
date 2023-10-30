import numpy as np

import errors.errors as err
import utils.constants as abb
from domain.tutoringModel import utils


class GeneticAlgorithm:
    """The Genetic Algorithm class simulates the process of natural
    selection using methods of evolutionary selection,
    combination and variation of individuals (Learning path)."""

    # learning path sequencing problem will be considered as
    # a Traveling Salesman Problem (TSP) and the Learning Style
    # of the Student is used for creating Personalized and
    # adaptive learning paths.

    def __init__(
        self,
        learning_elements=None,
    ):
        self.learning_elements = learning_elements
        self.learning_style = {}
        self.best_population = []
        self.le_coordinate: np.ndarray = np.array([])
        self.n_generation = 100
        self.population: np.ndarray = np.array([])
        self.le_size = 0
        self.mutate_rate = 0.3
        self.cross_rate = 0.9
        self.pop_size = 80
        if learning_elements is not None:
            #  convert learning element into
            #  a list with the short name of learning element
            le = self.get_learning_element(learning_elements)
            self.le_size = len(le)

    def create_random_population(self, dict_coordinates) -> None:
        """Function for the calculation of the score.
        position a also Initialise some populations
        with Clustering if this is possible.
        param dict_coordinates"""
        self.le_coordinate = np.array(
            [dict_coordinates[key] for key in dict_coordinates]
        )
        self.le_coordinate.reshape((len(dict_coordinates), 4))
        self.population = utils.permutation_generator(self.le_size, self.pop_size)

    def valide_population(self):
        """Function to add validation: First Learning Element is fixed
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
        """Function to calculate the fitness function for GA"""
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
        """Function for the calculation of crossovers between
        each individual."""
        # two parents are randomly selected from the population,
        # to inherit a part of their solution to their child.

        if np.random.rand() < self.cross_rate:
            samples = 2
            i_ = utils.random_generator(samples, size=1, type_="int")
            # choose crossover learning elements
            temp = self.le_size - 1
            cross_points = utils.random_generator(2, size=temp, type_="bool")
            keep_le = parent[~cross_points]
            swap_le = pop[i_, np.isin(pop[i_].ravel(), keep_le, invert=True)]
            parent = np.concatenate((keep_le, swap_le))
        return parent

    def mutate(self, child):
        """To prevent all offspring of a new generation
        from having the same approximation, a percentage
        probability is set at which an offspring will receive
        a mutation"""
        # In this case, two points within the pathway
        # are exchanged. This creates a new pathway that
        # may not appear in the previous generation
        temp = self.le_size - 2
        for point in range(temp):
            rate = utils.random_generator(0, 1, "float")
            if rate < self.mutate_rate:
                swap_point = utils.random_generator(2, temp, "int")
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

    def calculate_learning_path_ga(self, learning_style):
        """This function calculates the learning path with Genetic algorithm"""
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

            if best_score < best_total_score and i < self.n_generation:
                best_total_score = best_score
                self.best_population = best_sample

            # evolution
            self.evolve(fitness, best_sample)

        ga_path = np.array(self.learning_elements)
        population = self.valide_population()
        idx = population[0]
        result_ga_lp = ga_path[idx]

        learning_path = self.get_learning_path_as_str(result_ga_lp)

        return learning_path

    def get_learning_path_as_str(self, result_ga):
        """Convert the list of learning path into sting"""
        str_learning_path = ""
        contain_le = False
        for ele in result_ga:
            str_learning_path = str_learning_path + ele + ", "
            contain_le = True
        if contain_le:
            str_learning_path = str_learning_path[:-2]

        return str_learning_path

    def get_learning_style(self, learning_style):
        """Convert the dictionary into another format
        with the dimension and value for Genetic algorithm"""
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
        """Checks if the learning styles
        have values between 0 and 11"""
        is_correct = False
        for iterator in input_learning_style:
            if input_learning_style.get(iterator):
                dimension_number = input_learning_style.get(iterator)
                if dimension_number < 0 or dimension_number > 11:
                    is_correct = True
                    break

        return is_correct

    def check_name_learning_style(self, input_learning_style):
        """Check if the names of learning styles are correct."""
        pairs = [
            {"act", "ref"},
            {"sns", "int"},
            {"vis", "vrb"},
            {"seq", "glo"},
        ]
        return any(
            [
                True if set(pair).issubset(input_learning_style) else False
                for pair in pairs
            ]
        )

    def get_learning_element(self, learning_elements):
        """converts the dictionary learning element
        into a list with only the short name LE"""
        classification_learning_element = []
        lz_is_present = False
        lz_element = ""

        for le in learning_elements:
            if le["classification"] == abb.abbreviation_ct:
                classification_learning_element.insert(0, le["classification"])
            elif le["classification"] == abb.abbreviation_as:
                lz_is_present = True
                lz_element = le["classification"]
            else:
                classification_learning_element.append(le["classification"])

        if lz_is_present:
            classification_learning_element.append(lz_element)

        return classification_learning_element

    def get_learning_path(self, input_learning_style=None, input_learning_element=None):
        """calculates and verifies the learning path the genetic algorithm"""
        result_ga = []
        if input_learning_style is None:
            raise err.MissingParameterError()
        else:
            learning_style = self.get_learning_style(input_learning_style)
            if len(learning_style) != 4:
                raise err.WrongLearningStyleNumberError()

            if self.check_learning_style(learning_style):
                raise err.WrongLearningStyleDimensionError()

            if self.check_name_learning_style(learning_style):
                raise err.WrongParameterValueError()

        if input_learning_element is None:
            raise err.NoValidParameterValueError()
        else:
            self.learning_elements = self.get_learning_element(input_learning_element)
            self.le_size = len(self.learning_elements)

        result_ga = self.calculate_learning_path_ga(input_learning_style)
        return result_ga
