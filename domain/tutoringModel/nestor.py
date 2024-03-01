# LIBARIES:
# import argparse
# import sys
# import time
import os
import random
import sys

from pgmpy.inference import VariableElimination
from pgmpy.readwrite import XMLBIFReader

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..//")
# import examples_learning_elements as e_le  # nopep8
# import examples_learning_style as e_ls  # nopep8

# random.seed(143)


class Nestor:
    """
    This class is defined to implement the
    CausalNestor algorithm
    """

    def __init__(self):
        """
        All the global values used in Nestor
        are initiated here.
        """
        # the following are the LE formats used in RGB
        self.rgb_le_variables = [
            "CT",
            "BO",
            "LG",
            "MS",
            "QU",
            "EX",
            "SU",
            "AAM",
            "VAM",
            "TAM",
        ]
        # Loading the saved BN from local disk
        # self.path_to_model = os.path.join(
        #     "Nestor",
        #     "name3_saved_bn.xml"
        # )
        # In case BFI and/or LIST-k is used
        # this dict is used to decode the numerical values
        self.likert_scale = {
            1: "strong_disagree",
            2: "disagree",
            3: "neither_agree_disagree",
            4: "agree",
            5: "strong_agree",
        }
        # the following dict is used to map
        # output variables' states of trained BN with LE formats
        # used in HASKI.
        self.le_name_map_rgb_to_common_HASKI = {
            "{'CT': 'Yes'}": ["FO"],
            "{'CT': 'No'}": ["FO"],
            "{'BO': 'Yes'}": ["KÜ"],
            "{'BO': 'No'}": ["KÜ"],
            "{'LG': 'Yes'}": ["LZ"],
            "{'LG': 'No'}": ["LZ"],
            # the manuscript is mapped with three LE from common HASKI
            # so a random weighted selection of this LE is made below
            "{'MS': 'Yes'}": random.choices(
                ["EK", "AB", "BE"], weights=[0.8, 0.1, 0.1]
            ),
            "{'MS': 'No'}": random.choices(["EK", "AB", "BE"], weights=[0.8, 0.1, 0.1]),
            # "{'QU': 'Yes'}": ["RQ", "SE"],
            # "{'QU': 'No'}": ["RQ", "SE"],
            "{'QU': 'Yes'}": ["RQ"],
            "{'QU': 'No'}": ["RQ"],
            "{'EX': 'Yes'}": ["ÜB"],
            "{'EX': 'No'}": ["ÜB"],
            "{'SU': 'Yes'}": ["ZF"],
            "{'SU': 'No'}": ["ZF"],
            # the additional auditive material states
            # are not mapped to any LE formats
            # "{'AAM': 'Yes'}": ["AN"],
            # "{'AAM': 'No'}": ["AN"],
            "{'VAM': 'Yes'}": ["AN"],
            "{'VAM': 'No'}": ["AN"],
            "{'TAM': 'Yes'}": ["ZL"],
            "{'TAM': 'No'}": ["ZL"],
        }
        # this dict maps output variable states of BN
        # to RGB LE formats
        self.le_name_map = {
            "{'CT': 'Yes'}": "kollaborativ",
            "{'BO': 'Yes'}": "kurzuebersicht",
            "{'LG': 'Yes'}": "lernziele",
            "{'MS': 'Yes'}": "manuskript",
            "{'QU': 'Yes'}": "quiz",
            "{'EX': 'Yes'}": "uebung",
            "{'SU': 'Yes'}": "zusammenfassung",
            "{'AAM': 'Yes'}": "zusatzmaterial_auditiv",
            "{'VAM': 'Yes'}": "zusatzmaterial_visuell",
            "{'TAM': 'Yes'}": "zusatzmaterial_textuell",
        }
        # this dict maps FSLSM model learning style nomenclature
        # used in HASKI to nomenclature
        # used in training Nestor.
        self.ls_map_common_HASKI_to_nestor = {
            "act": "Active",
            "ref": "Reflective",
            "sns": "Sensory",
            "int": "Intuitive",
            "vis": "Visual",
            "vrb": "Verbal",
            "seq": "Sequential",
            "glo": "Global",
        }
        # self.random_seed = random.seed(143)

    def train_nestor(self):
        """This function is used to train the BN and save weights locally
        The saved weights are further used by the get_learning_path method
        to return the learning path
        """
        print(
            "The scripts used for training is stored in a seperate folder"
            "along with helper functions and configuration variables"
        )
        # Building the Topology of BN for Psychological models
        # bn = build_bn(edges_list=edges_list_only_psy_models)

        # # Training the BN for leanring the CPDs
        # train_bn(data=df_data_categories, model_bn=bn,
        #          state_names=state_names_bn_training_psy_model,
        #          estimator=EM)

        # # Extending the Topology of BN to LEs
        # bn = extend_bn_to_le(
        #     network=bn,
        #     edges_active_reflective=edges_list_active_reflective,
        #     edges_sensory_intuitive=edges_list_sensory_intuitive,
        #     edges_visual_verbal=edges_list_visual_verbal,
        #     edges_sequential_global=edges_list_sequential_global
        #                      )

        # # Defining the CPDs manually for LEs
        # bn.add_cpds(
        #     cpd_ct, cpd_bo, cpd_lg, cpd_ms, cpd_qu,
        #     cpd_ex, cpd_su, cpd_aam, cpd_tam, cpd_vam
        #             )

        # print("\nWriting trained BN to local folder\n")
        # # Writing the BN to a local folder
        # writer = XMLBIFWriter(bn)
        # writer.write_xmlbif(filename=path_to_trainedmodel)
        # return bn
        return None

    def get_learning_path(  # noqa: C901
        self,
        input_learning_style=None,
        input_learning_elements=None,
        path_to_model=os.path.join("Nestor", "name3_saved_bn.xml"),
    ):
        """
        This function reads in pre-processed information
        of learner
        to recommend personalized learning paths
        """
        # defining the path to saved BN
        path_to_model = path_to_model
        # The HASKI Gemeninsam uses the Learning styles naming convention of
        # (act, ref, sen, int, vis, vrb, seq, glo).
        # The Nesor uses a naming convention of
        # (Active, Reflective, Sensory, Intuitive,
        # Visual, Verbal, Sequential, Global)
        # Below a dict is used to map this naming convention for giving
        # the evidence on student to nestor
        evidence_for_inference = {
            "Active_Reflective_Dim": self.ls_map_common_HASKI_to_nestor[
                input_learning_style["processing_dimension"]
            ],
            "Sensory_Intuitive_Dim": self.ls_map_common_HASKI_to_nestor[
                input_learning_style["perception_dimension"]
            ],
            "Visual_Verbal_Dim": self.ls_map_common_HASKI_to_nestor[
                input_learning_style["input_dimension"]
            ],
            "Sequential_Gloabl_Dim": self.ls_map_common_HASKI_to_nestor[
                input_learning_style["understanding_dimension"]
            ],
            # the values of BFI and LIST-K are not given as evidences
            # "bfie": str(bfie_val),
            # "bfia": str(bfia_val),
            # "bfin": str(bfin_val),
            # "bfic": str(bfic_val),
            # "bfio": str(bfio_val),
            # "ks": str(ks_val),
            # "mks": str(mks_val),
            # "smir": str(smir_val),
            # "smer": str(smer_val)
        }
        # local variables
        le_max_dict = {}
        # yes_keys = []
        # updated_le_max_dict = {}
        # Initialize an empty dictionary to store the sorted key-value pairs
        le_sorted_dict = {}
        # updating the LE names with tags used in common HASKI
        le_renamed_dict = {}
        # the following list is used to store LE formats from
        # input LE param of this method
        # Careful! - this list might contain duplicate LEs
        le_format_duplicates = []
        # the following list contains no duplicated values
        # if the input LE param of this method has no duplicates natively,
        # this following list will be an extra operation
        le_format_no_duplicates = []
        # In mapping HASKI LEs with RGB LEs,
        # more than one HASKI LEs are mapped to a few RGB LEs
        # The union of non-duplicated HASKI LEs and RGB LEs,
        # are recommended with highest prob. first,
        # and least at the end as final learning path
        le_path = []
        # post processing the learning path to a sting
        output_string = ""
        # Inference Start
        # print("\n****START- Loading PGMPY Model****")
        # sTime = time.time()
        # preparing the learning elements
        # the input param for LEs is a list of LEs (Learning path)
        # Each LE in learning path is a dict. and
        # the "classification" key returns the format of LE
        for ele_ in input_learning_elements:
            le_format_duplicates.append(ele_["classification"])
        # check for duplicate LE formats and remove them
        for ele_ in le_format_duplicates:
            if ele_ not in le_format_no_duplicates:
                le_format_no_duplicates.append(ele_)
        # start inference with BN
        bn = XMLBIFReader(path_to_model).get_model()
        le_infer = VariableElimination(bn)
        # looping each le to estimate its probability of recommending
        for le in range(len(self.rgb_le_variables)):
            # To query the joint probabilities
            # query_all = le_infer.query(
            #     variables=[le_variables[le]],
            #     evidence= evidence_for_inference,
            #     joint= False
            # )
            # To query the LE format (übersicht, lernziel, etc.)
            query_map = le_infer.map_query(
                variables=[self.rgb_le_variables[le]],
                evidence=evidence_for_inference,
                show_progress=False,
            )
            # To query the probability values
            query_max = le_infer.max_marginal(
                variables=[self.rgb_le_variables[le]],
                evidence=evidence_for_inference,
                show_progress=False,
            )
            # creating a dict with LE and their probabilities.
            le_max_dict[str(query_map)] = str(query_max)
        # le_max_dict.pop(str({'CT': 'Yes'}))
        # The RGB LEs AAM and VAM are mapped with Animation.
        # 70% of times, AN is VAM and 30% of times AN is AAM
        # Removing the AAM from recommending since it has
        # no mapping with HASKI common LEs.
        # Workflow as follows:
        # if both AAM and VAM are present in the le_max dict:
        # 70% of times remove AAM and 30% of times remove VAM
        if str({"VAM": "Yes"}) and str({"AAM": "Yes"}) in le_max_dict:
            ele_to_remove = random.choices(
                [str({"VAM": "Yes"}), str({"AAM": "Yes"})], weights=[0.7, 0.3]
            )
            try:
                le_max_dict.pop(ele_to_remove[0])
            except KeyError:
                le_max_dict.update(ele_to_remove[0])

        elif str({"VAM": "Yes"}) and str({"AAM": "No"}) in le_max_dict:
            ele_to_remove = random.choices(
                [str({"VAM": "Yes"}), str({"AAM": "No"})], weights=[0.7, 0.3]
            )
            try:
                le_max_dict.pop(ele_to_remove[0])
            except KeyError:
                le_max_dict.update(ele_to_remove[0])

        elif str({"VAM": "No"}) and str({"AAM": "Yes"}) in le_max_dict:
            ele_to_remove = random.choices(
                [str({"VAM": "No"}), str({"AAM": "Yes"})], weights=[0.7, 0.3]
            )
            try:
                le_max_dict.pop(ele_to_remove[0])
            except KeyError:
                le_max_dict.update(ele_to_remove[0])

        elif str({"VAM": "No"}) and str({"AAM": "No"}) in le_max_dict:
            ele_to_remove = random.choices(
                [str({"VAM": "No"}), str({"AAM": "No"})], weights=[0.7, 0.3]
            )
            try:
                le_max_dict.pop(ele_to_remove[0])
            except KeyError:
                le_max_dict.update(ele_to_remove[0])
        # start - old approach - always map RGB-VAM to Animation.
        # if str({'AAM': 'Yes'}) in le_max_dict:
        #     le_max_dict.pop(str({'AAM': 'Yes'}))
        # elif str({'AAM': 'No'}) in le_max_dict:
        #     le_max_dict.pop(str({'AAM': 'No'}))
        # end old approach
        # print('\nPrinting the keys with yes and no', le_max_dict)
        # here the dictionary contains inference with both yes and no
        # The LEs with state 'No' is not removed but
        # probability for state 'yes' is calculated
        for key in le_max_dict.keys():
            # if 'Yes' in key:
            #     yes_keys.append(key)
            # if there is 'No' in the keys:
            # subract its value with 1 to find
            # prob. of recommedning that LE.
            if "No" in key:
                le_max_dict[key] = str(round(1 - float(le_max_dict[key]), 1))
                # yes_keys.append(key)
        # for val_ in yes_keys:
        #     le_max_dict[val_]
        #     updated_le_max_dict[val_] = le_max_dict[val_]
        # arraning dict in decending order
        # Get items from the input_dict and
        # sort them based on the numerical values in descending order
        sorted_items = sorted(
            le_max_dict.items(), key=lambda item: float(item[1]), reverse=True
        )
        # Iterate through the sorted items and populate the sorted_dict
        for key, value in sorted_items:
            le_sorted_dict[key] = value
        # print("\nCheck if the dict is in descending order: ",
        # le_sorted_dict)
        # renaming the LE formats to match HASKi common
        for key, val in le_sorted_dict.items():
            updated_key = random.choice(
                self.le_name_map_rgb_to_common_HASKI.get(key, key)
            )
            le_renamed_dict[updated_key] = val
        le_renamed = []
        for key_ in le_renamed_dict:
            le_renamed.append(key_)
        # Removing the learning elements from learning path
        # if they are not present in the HASKI server
        # for ele in le_renamed:
        #     print(ele)
        #     if ele not in le_format_no_duplicates:
        #         le_renamed.remove(ele)
        for ele in le_renamed:
            # for le_ in le_format_duplicates:
            if ele in le_format_no_duplicates:
                le_path.append(ele)
        for key_ in le_path:
            output_string = output_string + key_ + ", "
        # removing last two characters of final string
        output_string = output_string[:-2]
        print(output_string)
        # return le_renamed_dict
        return output_string
