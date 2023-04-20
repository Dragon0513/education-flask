from domain.tutoringModel import model as tutoringModel
from domain.domainModel import model as LE
import numpy as np


ele = ["KÜ", "LK", "ZF", "RQ", "SE", "FO", "ZL", "AN", "ÜB", "BE", "AB", "LZ"]

graf = {
    "RQ": (-1, 1, 0, 1, 0, 0, 0, 0),  # RQ
    "SE": (1, -1, 1, 0, 0, 0, 0, 0),  # SE
    "FO": (1, -1, 0, -1, -1, 1, 0, 0),  # FO
    "ZL": (-1, 1, -1, 1, -1, 1, 0, 0),  # ZL
    "AN": (1, -1, 1, -1, 1, -1, 0, 0),  # AN
    "ÜB": (1, -1, 1, 1, 0, 0, 0, 0),  # ÜB
    "BE": (-1, 1, 1, -1, 0, 0, 0, 1),  # BE
    "AB": (0, 0, 1, -1, 0, 0, 0, 1)  # AB
}


def get_coordinates(learning_style, learning_elements):
    coordinates = {}
    for elememnt in learning_elements:
        if elememnt == "KÜ":
            coordinates['KÜ'] = (13, 13, 13, 13)
        elif elememnt == "LK":
            coordinates['LK'] = (12, 12, 12, 12)
        elif elememnt == "LZ":
            coordinates['LZ'] = (-12, -12, -12, -12)
        elif elememnt == "ZF":
            if('REF' in learning_style.keys() and 'SEQ' in learning_style.keys()):
                if learning_style['REF'] > learning_style['SEQ']:
                    coordinates['ZF'] = (11, 11, 11, 11)
                else:
                    coordinates['ZF'] = (0, 0, 0, 0)
            else:
                coordinates['ZF'] = (11, 11, 11, 11)
        else:
            coordinate = list()
            for key in learning_style.keys():
                if key == "ACT":
                    coordinate.append(
                        learning_style['ACT'] * graf[elememnt][0])
                elif key == "REF":
                    coordinate.append(
                        learning_style['REF'] * graf[elememnt][1])
                if key == "SNS":
                    coordinate.append(
                        learning_style['SNS'] * graf[elememnt][2])
                elif key == "INT":
                    coordinate.append(
                        learning_style['INT'] * graf[elememnt][3])
                if key == "VIS":
                    coordinate.append(
                        learning_style['VIS'] * graf[elememnt][4])
                elif key == "VRB":
                    coordinate.append(
                        learning_style['VRB'] * graf[elememnt][5])
                if key == "SEQ":
                    coordinate.append(
                        learning_style['SEQ'] * graf[elememnt][6])
                elif key == "GLO":
                    coordinate.append(
                        learning_style['GLO'] * graf[elememnt][7])
            coordinates[elememnt] = tuple(coordinate)
    return coordinates


def get_coordinate(learning_style, learning_elements):

    dict_coordinates = get_coordinates(learning_style, learning_elements)
    ele = len(learning_elements)
    GA_coordinates = np.zeros((ele, 4))
    idx = 0
    for key in dict_coordinates.keys():
        GA_coordinates[idx, :] = dict_coordinates[key]
        idx = idx+1

    return GA_coordinates


def check_learning_style(input_learning_style):

    is_correct = False
    for iterator in input_learning_style:

        if (input_learning_style.get(iterator)):

            dimension_number = input_learning_style.get(iterator)
            if (dimension_number < 0 or dimension_number > 11):
                is_correct = True
                break

    return is_correct


def check_name_learning_style(input_learning_style):

    is_correct = False
    list_is_correct = []

    for iterator in input_learning_style:

        condition1 = (iterator == 'ACT' or iterator == 'REF')
        condition2 = (iterator == 'SNS' or iterator == 'INT')
        condition3 = (iterator == 'VIS' or iterator == 'VERB')
        condition4 = (iterator == 'SEQ' or iterator == 'GLO')
        if(condition1):
            list_is_correct.append(True)
        if(condition2):
            list_is_correct.append(True)
        if(condition3):
            list_is_correct.append(True)
        if(condition4):
            list_is_correct.append(True)

    temp = [True, True, True, True]
    if(list_is_correct != temp):
        is_correct = True

    return is_correct


def get_dict_Learning_element():

    elements = ["KÜ", "LK", "ZF", "RQ", "SE",
                "FO", "ZL", "AN", "ÜB", "BE", "AB", "LZ"]
    id = 0
    dict_Learning_element = {}
    for ele in elements:
        LearningElement = LE.LearningElement(lms_id=None,
                                             activity_type=None,
                                             classification=ele,
                                             name=ele,
                                             university=None,
                                             created_by=None,
                                             created_at=None,
                                             last_updated=None,
                                             )
        LearningElement.id= id                                  
        dict_Learning_element[ele] = LearningElement
        id = id+1
    return dict_Learning_element


def get_list_LPLE(learning_path, dict_Learning_element, LP_id):

    if(dict_Learning_element is None):
        dict_Learning_element = get_dict_Learning_element()

    List_LPLE = []
    for key in learning_path:
        condition = dict_Learning_element.get(key) is not None
        if (condition):
            element = dict_Learning_element.get(key)
            LPLE = tutoringModel.LearningPathLearningElement(learning_element_id=element.id,
                                                             learning_path_id=LP_id,
                                                             recommended=True,
                                                             position=None)
            List_LPLE.append(LPLE)
    #print("List_LPLE: ",[i.learning_element_id for i in List_LPLE])
    return List_LPLE


def get_learning_style( learning_style):
    print("### get_learning_style")
    
    result = {}
    if(learning_style.processing_dimension == "act"):
        result["act"] = learning_style.processing_value
    else:
        result["ref"] = learning_style.processing_value

    if(learning_style.perception_dimension == "sns"):
        result["sns"] = learning_style.perception_value
    else:
        result["int"] = learning_style.perception_value

    if(learning_style.input_dimension == "vis"):
        result["vis"] = learning_style.input_value
    else:
        result["vrb"] = learning_style.input_value    

    if(learning_style.understanding_dimension == "glo"):
        result["glo"] = learning_style.understanding_value
    else:
        result["seq"] = learning_style.understanding_value
    
    print("###get_learning_style",result)
    print(result)
    return result    


def get_learning_element( learning_elements):
    result = []
    print("### get_learning_element")
    for ele in learning_elements:            
        print("*****",ele.classification," ", type(learning_elements))
        result.append(ele.classification)
    print(result)
    print("###learning_elements",result)
    return result   

