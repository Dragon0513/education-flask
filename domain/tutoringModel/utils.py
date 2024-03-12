import math
from datetime import datetime

import numpy as np

import errors.errors as err
from utils import constants as cons

rng = np.random.default_rng(5)

ran_seed = int(datetime.timestamp(datetime.now()))

# Interpretation of Graf et al. for Learning Elements
# -1: negative Influence; 0: neutral; 1: positive Influence
# ACT-REF-SNS-INT-VIS-VRB-SEQ-GLO
influence = {
    "RQ": (-1, 1, 0, 1, 0, 0, 0, 0),
    "SE": (1, -1, 1, 0, 0, 0, 0, 0),
    "FO": (1, -1, 0, -1, -1, 1, 0, 0),
    "ZL": (-1, 1, -1, 1, -1, 1, 0, 0),
    "AN": (1, -1, 1, -1, 1, -1, 0, 0),
    "ÜB": (1, -1, 1, 1, 0, 0, 0, 0),
    "BE": (-1, 1, 1, -1, 0, 0, 0, 1),
    "AB": (0, 0, 1, -1, 0, 0, 0, 1),
}


# Calculate the coordinates for the LEs
def get_coordinates(learning_style, list_of_les):
    coordinates = {}
    for elememnt in list_of_les:
        if elememnt == cons.abbreviation_ct:
            coordinates[cons.abbreviation_ct] = (13, 13, 13, 13)
        elif elememnt == cons.abbreviation_co:
            coordinates[cons.abbreviation_co] = (12, 12, 12, 12)
        elif elememnt == cons.abbreviation_as:
            coordinates[cons.abbreviation_as] = (-12, -12, -12, -12)
        elif elememnt == cons.abbreviation_cc:
            if (
                learning_style["processing_dimension"] == "ref"
                and learning_style["understanding_dimension"] == "seq"
            ):
                if (
                    learning_style["processing_value"]
                    > learning_style["understanding_value"]
                ):
                    coordinates[cons.abbreviation_cc] = (11, 11, 11, 11)
                else:
                    coordinates[cons.abbreviation_cc] = (0, 0, 0, 0)
            elif (
                learning_style["processing_dimension"] == "ref"
                or learning_style["understanding_dimension"] == "glo"
            ):
                coordinates[cons.abbreviation_cc] = (11, 11, 11, 11)
            else:
                coordinates[cons.abbreviation_cc] = (0, 0, 0, 0)
        else:
            coordinate = list()
            if learning_style["processing_dimension"] == "act":
                coordinate.append(
                    learning_style["processing_value"] * influence[elememnt][0]
                )
            elif learning_style["processing_dimension"] == "ref":
                coordinate.append(
                    learning_style["processing_value"] * influence[elememnt][1]
                )
            if learning_style["perception_dimension"] == "sns":
                coordinate.append(
                    learning_style["perception_value"] * influence[elememnt][2]
                )
            elif learning_style["perception_dimension"] == "int":
                coordinate.append(
                    learning_style["perception_value"] * influence[elememnt][3]
                )
            if learning_style["input_dimension"] == "vis":
                coordinate.append(
                    learning_style["input_value"] * influence[elememnt][4]
                )
            elif learning_style["input_dimension"] == "vrb":
                coordinate.append(
                    learning_style["input_value"] * influence[elememnt][5]
                )
            if learning_style["understanding_dimension"] == "seq":
                coordinate.append(
                    learning_style["understanding_value"] * influence[elememnt][6]
                )
            elif learning_style["understanding_dimension"] == "glo":
                coordinate.append(
                    learning_style["understanding_value"] * influence[elememnt][7]
                )
            coordinates[elememnt] = tuple(coordinate)
    return coordinates


# Euclidean Distance Function
def distance(xyz1, xyz2) -> float:
    if isinstance(xyz1[0], str):
        xyz1 = xyz1[1]
        xyz2 = xyz2[1]
    return math.dist(xyz1, xyz2)


def permutation_generator(le_size, pop_size):
    """function to randomly generate population for ga"""
    positions = np.arange(1, le_size)
    perm = rng.permutation(positions)
    population = np.tile(perm, (pop_size, 1))
    return population


def random_generator(num, size, type_):
    if type_ == "int":
        return rng.integers(0, num, size=1)

    elif type_ == "bool":
        return rng.choice([True, False], size)
    else:
        raise err.WrongParameterValueError()


def check_learning_style(input_learning_style):
    """ Check if learning style is correctly formatted and\
    has the right dimensions"""
    condition1 = cons.name_perception_dimension in input_learning_style.keys()
    condition2 = cons.name_input_dimension in input_learning_style.keys()
    condition3 = cons.name_processing_dimension in input_learning_style.keys()
    condition4 = cons.name_understanding_dimension in input_learning_style.keys()
    condition5 = cons.name_perception_value in input_learning_style.keys()
    condition6 = cons.name_input_value in input_learning_style.keys()
    condition7 = cons.name_processing_value in input_learning_style.keys()
    condition8 = cons.name_understanding_value in input_learning_style.keys()
    if not (
        condition1
        and condition2
        and condition3
        and condition4
        and condition5
        and condition6
        and condition7
        and condition8
    ):
        raise err.WrongLearningStyleNumberError()
    condition9 = -11 <= input_learning_style[cons.name_perception_value] <= 11
    condition10 = -11 <= input_learning_style[cons.name_input_value] <= 11
    condition11 = -11 <= input_learning_style[cons.name_processing_value] <= 11
    condition12 = -11 <= input_learning_style[cons.name_understanding_value] <= 11
    if not (condition9 and condition10 and condition11 and condition12):
        raise err.WrongLearningStyleDimensionError()
    else:
        return True


def get_learning_path_as_str(result_ga):
    """Convert the list of learning path into sting"""
    str_learning_path = ""
    contain_le = False
    for ele in result_ga:
        str_learning_path = str_learning_path + ele + ", "
        contain_le = True
    if contain_le:
        str_learning_path = str_learning_path[:-2]

    return str_learning_path
