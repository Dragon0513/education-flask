import math

import numpy as np

from utils import constants as cons

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

# function to randomly generate the population for ga
def permutation_generator(le_size, pop_size):
    positions = np.arange(1, le_size)
    population = np.vstack(
        [np.random.permutation(positions)
         for _ in range(pop_size)])
    return population

def ramdon_generator( num, size, type_):
    if type_ == 'decimal':
        return np.random.rand()
    if type_ == 'int':
        return np.random.randint(0, num, size=1)
    if type_ == 'bool':
        return np.random.randint(0, num, size).astype(bool)
    else:
        return 0
