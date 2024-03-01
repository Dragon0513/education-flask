import numpy as np

from domain.tutoringModel.Tyche import tyche_config as t_config
from domain.tutoringModel.Tyche import tyche_utils as t_utils
from errors import errors as err


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
            if curr_le == "KÜ":
                classification_learning_element[0] = "kurzuebersicht"
            elif curr_le == "LZ":
                classification_learning_element[1] = "lernziele"
            elif curr_le == "EK":
                classification_learning_element[2] = "manuskript_ek"
            elif curr_le == "AB":
                classification_learning_element[3] = "manuskript_ab"
            elif curr_le == "BE":
                classification_learning_element[4] = "manuskript_be"
            elif curr_le == "RQ":
                classification_learning_element[5] = "quiz_rq"
            elif curr_le == "SE":
                classification_learning_element[6] = "quiz_se"
            elif curr_le == "ÜB":
                classification_learning_element[7] = "uebung"
            elif curr_le == "ZF":
                classification_learning_element[8] = "zusammenfassung"
            elif curr_le == "ZL":
                classification_learning_element[9] = "zusatzmaterial_textuell"
            elif curr_le == "FO":
                classification_learning_element[10] = "kollaborativ"
            elif curr_le == "AN":
                classification_learning_element[11] = "animation"
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
        curr_le = 0
        for i in range(len(self.learningpath)):
            curr_le = self.learningpath[i]
            if curr_le == "kurzuebersicht":
                curr_le = "KÜ"
            elif curr_le == "lernziele":
                curr_le = "LZ"
            elif curr_le == "manuskript_ek":
                curr_le = "EK"
            elif curr_le == "manuskript_ab":
                curr_le = "AB"
            elif curr_le == "manuskript_be":
                curr_le = "BE"
            elif curr_le == "quiz_rq":
                curr_le = "RQ"
            elif curr_le == "quiz_se":
                curr_le = "SE"
            elif curr_le == "uebung":
                curr_le = "ÜB"
            elif curr_le == "zusammenfassung":
                curr_le = "ZF"
            elif curr_le == "zusatzmaterial_textuell":
                curr_le = "ZL"
            elif curr_le == "animation":
                curr_le = "AN"
            else:
                print("Current learning element", curr_le, "is not part of our set!")
            self.learningpath[i] = curr_le
        pass

    def set_last_learning_element(self, classification_learning_element):
        if self.last_le:
            curr_le = self.last_le
            if curr_le == "KÜ":
                classification_learning_element[0] = "kurzuebersicht"
            elif curr_le == "LZ":
                classification_learning_element[1] = "lernziele"
            elif curr_le == "EK":
                classification_learning_element[2] = "manuskript_ek"
            elif curr_le == "AB":
                classification_learning_element[3] = "manuskript_ab"
            elif curr_le == "BE":
                classification_learning_element[4] = "manuskript_be"
            elif curr_le == "RQ":
                classification_learning_element[5] = "quiz_rq"
            elif curr_le == "SE":
                classification_learning_element[6] = "quiz_se"
            elif curr_le == "ÜB":
                classification_learning_element[7] = "uebung"
            elif curr_le == "ZF":
                classification_learning_element[8] = "zusammenfassung"
            elif curr_le == "ZL":
                classification_learning_element[9] = "zusatzmaterial_textuell"
            elif curr_le == "FO":
                classification_learning_element[10] = "kollaborativ"
            elif curr_le == "AN":
                classification_learning_element[11] = "animation"
            else:
                print("LE", curr_le, "is not part of our set!!")
        return classification_learning_element

    def get_learning_style(self):
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

    def get_learning_path_as_str(self):
        """Convert the list of learning path into sting"""
        str_learning_path = ""
        contain_le = False
        for ele in self.learningpath:
            str_learning_path = str_learning_path + ele + ", "
            contain_le = True
        if contain_le:
            str_learning_path = str_learning_path[:-2]
        return str_learning_path

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
        if "kollaborativ" in les:
            FO = True
            les.remove("kollaborativ")
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
            self.learningpath.append("FO")
        # Return learning path:

        learningpath = self.get_learning_path_as_str()
        return learningpath
