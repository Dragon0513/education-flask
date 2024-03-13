from pgmpy.estimators import ExpectationMaximization as EM
from pgmpy.models import BayesianNetwork

from utils.constants import likert_scale as likert_map

# Helper functions


def categorize_lisk_bfi(input_dataframe, encoding_columns):
    """
    This function decodes the nuerical responses of list-k and bfi
    to categories and suit PGMPY inference methods
    """
    # looping through rows
    for row in range(len(input_dataframe)):
        # looping through columns
        for col in input_dataframe.columns:
            if col in encoding_columns:
                input_dataframe.loc[row, col] = likert_map[
                    input_dataframe.loc[row, col]
                ]

    return input_dataframe


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
