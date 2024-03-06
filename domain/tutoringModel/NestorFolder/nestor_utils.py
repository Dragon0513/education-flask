# import pandas as pd
# import matplotlib.pyplot as plt
# import networkx as nx
# from pgmpy.estimators import BDeuScore
from pgmpy.estimators import ExpectationMaximization as EM

# from pgmpy.estimators import HillClimbSearch, MmhcEstimator, TreeSearch
from pgmpy.models import BayesianNetwork

# from pgmpy.estimators import PC, ExhaustiveSearch, K2Score


def categorize_lisk_bfi(input_dataframe, encoding_columns):
    """
    This function decodes the nuerical responses of list-k and bfi
    to categories and suit PGMPY inference methods
    """
    likert_map = {
        1: "strong_disagree",
        2: "disagree",
        3: "neither_agree_disagree",
        4: "agree",
        5: "strong_agree",
    }
    # looping through rows
    for each_row in range(len(input_dataframe)):
        # looping through columns
        for each_col in input_dataframe.columns:
            # print(input_dataframe.loc[each_row,each_col])
            if each_col in encoding_columns:
                input_dataframe.loc[each_row, each_col] = likert_map[
                    input_dataframe.loc[each_row, each_col]
                ]

    return input_dataframe


# Helper functions


def build_bn(edges_list: int, extend_structure=False):
    """This function reads the edges in form of a List of tuples
    and returns a built Bayesian Network"""

    bn = BayesianNetwork()
    bn.add_edges_from(ebunch=edges_list)
    print("\nType of Network:", type(bn))
    print("\nSuccess! - Built Bayesian Network with ICERI\n")
    return bn


# def build_bn_multiple_structures(edges_list, data, topology="algorithm"):
#     """This function reads the edges in form of a List of tuples
#     and returns a built Bayesian Network"""

#     if str(topology) == "iceri":
#         bn = BayesianNetwork()
#         bn.add_edges_from(ebunch=edges_list)
#         print("\nType of Network:", type(bn))
#         print("\nSuccess! - Built Bayesian Network with ICERI\n")
#         return bn

#     elif topology == "algorithm":
#         est = TreeSearch(data=data)
#         bn = est.estimate(estimator_type="chow-liu")
#         print("\nType of Network:", type(bn))
#         print("Success: Topology of BN built using Chow-Liu Tree Search")
#         model = BayesianNetwork(bn.edges())

#         return model

#     elif topology == "hybrid":
#         # initiate a Bayesian Network
#         bn = BayesianNetwork()
#         # Building Topology with Constraint Based Method
#         print("\nTopology Part 1: Constraint Based")
#         mmhc = MmhcEstimator(data=data)
#         skeleton = mmhc.mmpc()
#         # Orient the edges with a Score Based Method
#         # Using Hill climb method
#         hc = HillClimbSearch(data=data)
#         bn = hc.estimate(
#             tabu_length=10,
#             white_list=skeleton.to_directed().edges(),
#             scoring_method=BDeuScore(data=data),
#             show_progress=False,
#         )
#         print("\nTopology Part 2: Score Based")
#         print("\nType of Network:", type(bn))
#         print("\nSuccess: Topology of BN built using a Hybrid Strategy")
#         return bn

#     else:
#         print("Error: False Topology for Bayesian Network")


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
    # print("\nInput Type of Network:", type(network))
    print("\nExtending the Nestor topology to Learning Elements")
    network.add_edges_from(ebunch=edges_active_reflective)
    network.add_edges_from(ebunch=edges_sensory_intuitive)
    network.add_edges_from(ebunch=edges_visual_verbal)
    network.add_edges_from(ebunch=edges_sequential_global)
    # print("\nOutput Type of Network:", type(network))

    return network


# def visualize_bn(
#     bn_model,
#     with_labels=True,
#     arrowsize=30,
#     node_size=800,
#     alpha=0.3,
#     font_weight="bold",
# ):
#     """This function reads a bayesian model and visualizes
#     with the defined default parameters"""
#     nx.draw_circular(
#         bn_model,
#         with_labels=with_labels,
#         arrowsize=arrowsize,
#         node_size=node_size,
#         alpha=alpha,
#         font_weight=font_weight,
#     )
#     plt.show()


# TODO
# 1. Return specific error if the input data format is not pandas dataframe
# 2. Print which estimator is being utilized
# 3. Read state names from an external file (YAML?)


def train_bn(data, model_bn, state_names, estimator=EM):
    """This function reads the data in format pandas dataframe,
    bayesian model, estimator from pgmpy with state_names in type
    python dictionary. The input model is fitted with data with
    defined parameters and returned"""
    print(
        "\nStarting the Model training with" "defined data, estimator and parameters\n"
    )
    model_bn.fit(data=data, estimator=estimator, state_names=state_names)
    # print("\Done! - Model Training\n")
