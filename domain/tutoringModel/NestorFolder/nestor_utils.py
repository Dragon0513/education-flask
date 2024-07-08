import random
from collections import defaultdict

from pgmpy.estimators import ExpectationMaximization as EM
from pgmpy.models import BayesianNetwork

from domain.tutoringModel.utils import ran_seed

random.seed(ran_seed)
# Helper functions


def categorize_lisk_bfi(input_dataframe, encoding_columns):
    """
    This function decodes the nuerical responses of list-k and bfi
    to categories and suit PGMPY inference methods
    """
    # In case of BFI and/or LIST-k
    # this dict is used to decode the numerical values
    likert_map = {
        1: "strong_disagree",
        2: "disagree",
        3: "neither_agree_disagree",
        4: "agree",
        5: "strong_agree",
    }
    # looping through rows
    for row in range(len(input_dataframe)):
        # looping through columns
        for col in input_dataframe.columns:
            if col in encoding_columns:
                input_dataframe.loc[row, col] = likert_map[
                    input_dataframe.loc[row, col]
                ]

    return input_dataframe


def randomize_same_values(sorted_dict):
    """
    This function takes a dictionary sorted in descending order by its values.
    It randomizes the order of keys that have the same value while maintaining
    the overall descending order of different values.
    """
    # the probability values have string datatype
    # Convert string values to floats for comparison and sorting
    float_dict = {k: float(v) for k, v in sorted_dict.items()}

    # Group keys by their float values into a defaultdict(list)
    value_groups = defaultdict(list)
    for key, value in float_dict.items():
        value_groups[value].append(key)

    # Shuffle the keys within each group of the same value
    for key_group in value_groups.values():
        random.shuffle(key_group)

    # Reconstruct the dictionary in descending order by value,
    # keeping the randomized order within groups
    randomized_sorted_dict = {}
    # Sort and iterate in descending order
    for value in sorted(value_groups.keys(), reverse=True):
        for key in value_groups[value]:
            # Convert values back to strings
            randomized_sorted_dict[key] = str(value)

    return randomized_sorted_dict


def build_bn(edges_list):
    """This function reads the edges in form of a List of tuples
    and returns a built Bayesian Network"""

    bn = BayesianNetwork()
    bn.add_edges_from(ebunch=edges_list)
    print("\nModel's topology built.")
    return bn


# function to extend the network on top of learner data
def extend_bn_to_le(
    network,
    edges_active_reflective,
    edges_sensory_intuitive,
    edges_visual_verbal,
    edges_sequential_global,
):
    """
    This function intends to extend the structure to LE
    on top of the relationships between Learner Characteristics
    """
    all_edges = (
        edges_active_reflective
        + edges_sensory_intuitive
        + edges_visual_verbal
        + edges_sequential_global
    )
    network.add_edges_from(ebunch=all_edges)
    print("\nModel's topology extended for learning elements.")
    return network


def train_bn(data, model_bn, state_names, estimator=EM):
    """This function reads the data in format pandas dataframe,
    bayesian model, estimator from pgmpy with state_names in type
    python dictionary. The input model is fitted with data with
    defined parameters and returned"""
    print("\nStarting the Model training with defined data, estimator and parameters.")
    model_bn.fit(data=data, estimator=estimator, state_names=state_names)
    print("\nFinished Model Training!")
