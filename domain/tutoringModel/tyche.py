import numpy as np

from domain.tutoringModel import utils
from domain.tutoringModel.Tyche import tyche_config as t_config
from domain.tutoringModel.Tyche import tyche_utils as t_utils
from errors import errors as err
from utils import constants as cons


class TycheAlgorithm:
    """This algorithm calculates the learning path based on the\
        approach by Staufer et al. and is called Tyche algorithm.
    """

    def __init__(
        self,
        learning_elements=None,
    ):
        self.learning_elements = learning_elements
        self.learning_style = {}
        self.init_probabilities = []
        self.probabilities = []
        self.learningpath = []
        self.last_le = False

    def RGB_preprocessing(self):
        """converts the dictionary learning element
        into a list with only the short name of the LE"""
        classification_learning_element = ["none"] * 12

        for le in self.learning_elements:
            # Map learning elements:

            curr_le = le["classification"]
            if curr_le == cons.abbreviation_ct:
                classification_learning_element[0] = cons.name_kü
            elif curr_le == cons.abbreviation_as:
                classification_learning_element[1] = cons.name_lz
            elif curr_le == cons.abbreviation_co:
                classification_learning_element[2] = cons.name_ek
            elif curr_le == cons.abbreviation_ra:
                classification_learning_element[3] = cons.name_ab
            elif curr_le == cons.abbreviation_ex:
                classification_learning_element[4] = cons.name_be
            elif curr_le == cons.abbreviation_rq:
                classification_learning_element[5] = cons.name_rq
            elif curr_le == cons.abbreviation_se:
                classification_learning_element[6] = cons.name_se
            elif curr_le == cons.abbreviation_ec:
                classification_learning_element[7] = cons.name_üb
            elif curr_le == cons.abbreviation_cc:
                classification_learning_element[8] = cons.name_zf
            elif curr_le == cons.abbreviation_rm:
                classification_learning_element[9] = cons.name_zl
            elif curr_le == cons.abbreviation_fo:
                classification_learning_element[10] = cons.name_ko
            elif curr_le == cons.abbreviation_an:
                classification_learning_element[11] = cons.name_an
            else:
                print("LE", curr_le, "is not part of our set!!")
                raise err.WrongParameterValueError()
        classification_learning_element = self.set_last_learning_element(
            classification_learning_element
        )
        result_learning_element = []
        for i in classification_learning_element:
            if i != "none":
                result_learning_element.append(i)
        return result_learning_element

    def RGB_postprocessing(self):
        """converts the learning path to LE conventions
        of global HASKI"""
        curr_le = 0
        for i in range(len(self.learningpath)):
            curr_le = self.learningpath[i]
            if curr_le == cons.name_kü:
                curr_le = cons.abbreviation_ct
            elif curr_le == cons.name_lz:
                curr_le = cons.abbreviation_as
            elif curr_le == cons.name_ek:
                curr_le = cons.abbreviation_co
            elif curr_le == cons.name_ab:
                curr_le = cons.abbreviation_ra
            elif curr_le == cons.name_be:
                curr_le = cons.abbreviation_ex
            elif curr_le == cons.name_rq:
                curr_le = cons.abbreviation_rq
            elif curr_le == cons.name_se:
                curr_le = cons.abbreviation_se
            elif curr_le == cons.name_üb:
                curr_le = cons.abbreviation_ec
            elif curr_le == cons.name_zf:
                curr_le = cons.abbreviation_cc
            elif curr_le == cons.name_zl:
                curr_le = cons.abbreviation_rm
            elif curr_le == cons.name_an:
                curr_le = cons.abbreviation_an
            else:
                print("Current learning element", curr_le, "is not part of our set!")
            self.learningpath[i] = curr_le
        pass

    def set_last_learning_element(self, classification_learning_element):
        """Set the learning element"""
        if self.last_le:
            curr_le = self.last_le
            if curr_le == cons.abbreviation_ct:
                classification_learning_element[0] = cons.name_kü
            elif curr_le == cons.abbreviation_as:
                classification_learning_element[1] = cons.name_lz
            elif curr_le == cons.abbreviation_co:
                classification_learning_element[2] = cons.name_ek
            elif curr_le == cons.abbreviation_ra:
                classification_learning_element[3] = cons.name_ab
            elif curr_le == cons.abbreviation_ex:
                classification_learning_element[4] = cons.name_be
            elif curr_le == cons.abbreviation_rq:
                classification_learning_element[5] = cons.name_rq
            elif curr_le == cons.abbreviation_se:
                classification_learning_element[6] = cons.name_se
            elif curr_le == cons.abbreviation_ec:
                classification_learning_element[7] = cons.name_üb
            elif curr_le == cons.abbreviation_cc:
                classification_learning_element[8] = cons.name_zf
            elif curr_le == cons.abbreviation_rm:
                classification_learning_element[9] = cons.name_zl
            elif curr_le == cons.abbreviation_fo:
                classification_learning_element[10] = cons.name_ko
            elif curr_le == cons.abbreviation_an:
                classification_learning_element[11] = cons.name_an
            else:
                print("LE", curr_le, "is not part of our set!!")
        return classification_learning_element

    def get_learning_style(self):
        """Set the learning style in the format that
        Tyche needs"""
        lstyle = [0, 0, 0, 0]

        # Active-Reflective Dimension:
        dim1 = self.learning_style["processing_dimension"]
        if dim1 == "act":
            lstyle[0] = "active"
        elif dim1 == "ref":
            lstyle[0] = "reflective"
        else:
            print("Invalid value!")

        # Visual-Verbal Dimension:
        dim2 = self.learning_style["input_dimension"]
        if dim2 == "vis":
            lstyle[1] = "visual"
        elif dim2 == "vrb":
            lstyle[1] = "verbal"
        else:
            print("Invalid value!")

        # Sensing-Intuitive Dimension:
        dim3 = self.learning_style["perception_dimension"]
        if dim3 == "sns":
            lstyle[2] = "sensing"
        elif dim3 == "int":
            lstyle[2] = "intuitive"
        else:
            print("Invalid value!")

        # Sequential-Global Dimension:
        dim4 = self.learning_style["understanding_dimension"]
        if dim4 == "seq":
            lstyle[3] = "sequential"
        elif dim4 == "glo":
            lstyle[3] = "global"
        else:
            print("Invalid value!")
        return lstyle

    def get_probabilities(self, lstyle):
        """Get the probabilities of the learning element"""

        # Get initial state probability:
        a, b, c, d = 0, 0, 0, 0

        # Get further states probabilities:
        e, f, g, h = 0, 0, 0, 0  # Generic
        i, j, k, m = 0, 0, 0, 0  # Static
        if "active" in lstyle:
            a = np.array(t_config.Active_ini)
            e = np.array(t_config.Active_g)
            i = np.array(t_config.Active_static)
        elif "reflective" in lstyle:
            a = np.array(t_config.Reflective_ini)
            e = np.array(t_config.Reflective_g)
            i = np.array(t_config.Reflective_static)
        if "visual" in lstyle:
            b = np.array(t_config.Visual_ini)
            f = np.array(t_config.Visual_g)
            j = np.array(t_config.Visual_static)
        elif "verbal" in lstyle:
            b = np.array(t_config.Verbal_ini)
            f = np.array(t_config.Verbal_g)
            j = np.array(t_config.Verbal_static)
        if "intuitive" in lstyle:
            c = np.array(t_config.Intuitive_ini)
            g = np.array(t_config.Intuitive_g)
            k = np.array(t_config.Intuitive_static)
        elif "sensing" in lstyle:
            c = np.array(t_config.Sensing_ini)
            g = np.array(t_config.Sensing_g)
            k = np.array(t_config.Sensing_static)
        if "sequential" in lstyle:
            d = np.array(t_config.Sequential_ini)
            h = np.array(t_config.Sequential_g)
            m = np.array(t_config.Sequential_static)
        elif "global" in lstyle:
            d = np.array(t_config.Global_ini)
            h = np.array(t_config.Global_g)
            m = np.array(t_config.Global_static)

        # Arithmetic means:
        init_config = np.add(a, b)
        init_config = np.add(init_config, c)
        init_config = np.add(init_config, d)
        init_config = np.divide(init_config, 4.0)

        g_config = np.add(e, f)
        g_config = np.add(g_config, g)
        g_config = np.add(g_config, h)
        g_config = np.divide(g_config, 4.0)

        s_config = np.add(i, j)
        s_config = np.add(s_config, k)
        s_config = np.add(s_config, m)
        s_config = np.divide(s_config, 4.0)

        self.init_probabilities = init_config
        self.probabilities = g_config

    def get_learning_path(
        self, input_learning_style={}, input_learning_element=[], last_element=False
    ):
        """Inital method to start generating the learning path"""

        # Get learning style parameters:
        if input_learning_style == {}:
            raise err.MissingParameterError()
        else:
            self.learning_style = input_learning_style
        lstyle = self.get_learning_style()
        if 0 in lstyle:
            raise err.WrongParameterValueError()

        # Get learning elements:
        self.last_le = last_element
        if input_learning_element == []:
            raise err.NoValidParameterValueError()
        else:
            self.learning_elements = input_learning_element
        self.learning_elements = self.RGB_preprocessing()
        les = self.learning_elements

        # Get probabilities:
        self.get_probabilities(lstyle)

        # Set Forum as last learning element:
        FO = False
        if cons.name_ko in les:
            FO = True
            les.remove(cons.name_ko)

        # Calculate first node:
        if self.last_le:
            self.last_le = t_config.naming_map[self.last_le]
            start_node = self.last_le
        else:
            start_node = t_utils.get_startnode(self.init_probabilities, les)
            self.learningpath.append(start_node)

        # Calculate next nodes:
        lpath = t_utils.get_nextnodes(self.probabilities, les, start_node)
        if self.last_le:
            # delete last processed learning element from lpath:
            lpath = lpath[1:]

        # Map learning path to HASKI:
        self.learningpath = lpath
        self.RGB_postprocessing()

        # Add Forum as last learning element in learning path:
        if FO:
            self.learningpath.append(cons.abbreviation_fo)

        # Return learning path:
        learningpath_return = utils.get_learning_path_as_str(self.learningpath)
        return learningpath_return
