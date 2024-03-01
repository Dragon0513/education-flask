# Importing Libraries
import os

# import random
import sys

from pgmpy.estimators import ExpectationMaximization as EM
from pgmpy.readwrite import XMLBIFWriter

# sys.path.append("Nestor/") # nopep
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..//")
from Nestor.nestor_config import *  # nopep8
from nestor_utils import *  # nopep8

# from Dataloader import Get_course_data  # nopep8

print("\nImported all the Libraries")

# # TODO
# # 1. Return specific error if the input data format is not pandas dataframe
# # 2. Print which estimator is being utilized
# # 3. Read state names from an external file (YAML?)

# Building the Topology of BN for Psychological models
bn = build_bn(edges_list=edges_list_only_psy_models)

# Visualizing the Topology of BN
# visualize_bn(bn)

# Training the BN for leanring the CPDs
train_bn(
    data=df_data_categories,
    model_bn=bn,
    state_names=state_names_bn_training_psy_model,
    estimator=EM,
)

# Extending the Topology of BN to LEs
bn = extend_bn_to_le(
    network=bn,
    edges_active_reflective=edges_list_active_reflective,
    edges_sensory_intuitive=edges_list_sensory_intuitive,
    edges_visual_verbal=edges_list_visual_verbal,
    edges_sequential_global=edges_list_sequential_global,
)

# visualize the Built Bayesian Network
# visualize_bn(bn)

# Defining the CPDs manually for LEs
bn.add_cpds(
    cpd_ct, cpd_bo, cpd_lg, cpd_ms, cpd_qu, cpd_ex, cpd_su, cpd_aam, cpd_tam, cpd_vam
)

# Inference
# TODO
# 1. Recommend only one learning element with highest probability
# 2. When two or more LE have same probability
# value, randomize the recommendation
print("\nReading and Writing Network to local folder\n")

# Writing the BN to a local folder
writer = XMLBIFWriter(bn)
writer.write_xmlbif(filename=path_to_trainedmodel)
