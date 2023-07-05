from domain.tutoringModel import model as TM
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
                if key == "act":
                    coordinate.append(
                        learning_style['act'] * graf[elememnt][0])
                elif key == "ref":
                    coordinate.append(
                        learning_style['ref'] * graf[elememnt][1])
                if key == "sns":
                    coordinate.append(
                        learning_style['sns'] * graf[elememnt][2])
                elif key == "int":
                    coordinate.append(
                        learning_style['int'] * graf[elememnt][3])
                if key == "vis":
                    coordinate.append(
                        learning_style['vis'] * graf[elememnt][4])
                elif key == "vrb":
                    coordinate.append(
                        learning_style['vrb'] * graf[elememnt][5])
                if key == "seq":
                    coordinate.append(
                        learning_style['seq'] * graf[elememnt][6])
                elif key == "glo":
                    coordinate.append(
                        learning_style['glo'] * graf[elememnt][7])
            coordinates[elememnt] = tuple(coordinate)
    return coordinates


def get_coordinate(learning_style, learning_elements):

    dict_coordinates = get_coordinates(learning_style, learning_elements)
    #ele = ["KÜ", "LK", "ZF", "RQ", "SE", "FO", "ZL", "AN", "ÜB", "BE", "AB", "LZ"]

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

        condition1 = (iterator == 'act' or iterator == 'ref')
        condition2 = (iterator == 'sns' or iterator == 'int')
        condition3 = (iterator == 'vis' or iterator == 'vrb')
        condition4 = (iterator == 'seq' or iterator == 'glo')
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



def get_list_LPLE(learning_path, learning_elements, LP_id):

    # if(dict_Learning_element is None):
    #     dict_Learning_element = get_dict_Learning_element()

    List_LPLE = []
    for element in learning_elements:

        classification= element.classification
        condition = classification is not None
        condition2 = classification in learning_path
        
        if (condition and condition2 ):
            
            LPLE = TM.LearningPathLearningElement(learning_element_id=element.id,
                                                  learning_path_id=LP_id,
                                                  recommended=True,
                                                  position=learning_path.index(classification))
            #print(" classification: ",classification, " id: ",LPLE.learning_element_id," LPLE.position: ", LPLE.position )                                      
            List_LPLE.append(LPLE)

    #print("List_LPLE: ",[i.position for i in List_LPLE])
    return List_LPLE


def get_learning_style( learning_style):
   
    result = {}

    if(learning_style.get('processing_dimension')== "act"):
        result["act"] = learning_style.get('processing_value')
    else:
        result["ref"] = learning_style.get('processing_value')
  
    if(learning_style.get('perception_dimension') == "sns"):
        result["sns"] = learning_style.get('perception_value')
    else:
        result["int"] = learning_style.get('perception_value')

    if(learning_style.get('input_dimension') == "vis"):
        result["vis"] = learning_style.get('input_value')
    else:
        result["vrb"] = learning_style.get('input_value')   

    if(learning_style.get('understanding_dimension') == "glo"):
        result["glo"] = learning_style.get('understanding_value')
    else:
        result["seq"] = learning_style.get('understanding_value')
    


    for key, value in dict(result).items():
        if value == None:
            del result[key]   

    return result    



def add_Learning_element(learning_elements):
    #Initialize dictionary of learning Element zum test

    elements = ["KÜ", "LK", "ZF", "SE",
                "FO", "ZL", "AN", "ÜB", "BE", "AB", "LZ"]
    id = 0   

    for element in elements:
        LearningElement = LE.LearningElement(lms_id=id,
                                             activity_type=None,
                                             classification=element,
                                             name=element,
                                             university=None,
                                             created_by=None,
                                             created_at=None,
                                             last_updated=None,
                                             )
        LearningElement.id= id    
        learning_elements.add(LearningElement)
        #print("LE.",LearningElement.classification, " id: ", LearningElement.id, " element:",element)                       
        #dict_Learning_element[element] = LearningElement        
        id = id+1
   
    return learning_elements




def get_learning_element( learning_elements):   
    result = []    
    lz_is_present = True
    lz_element = ''
    #print("OBJECT-Learning Element--",type(learning_elements))        
    for le in learning_elements:            
        #print("1-Learning Element--",le.classification)
        if le.classification=='KÜ':
            result.insert(0,le.classification)
        elif  le.classification=='LZ':
            lz_is_present = True
            lz_element = le.classification
        else:    
            result.append(le.classification)

    if(lz_is_present):
        result.append(lz_element)       
   
    return result   

