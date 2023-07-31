import math
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
    "AB": (0, 0, 1, -1, 0, 0, 0, 1)
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
            if(learning_style['processing_dimension'] == 'ref'
               and learning_style['understanding_dimension'] == 'seq'):
                if learning_style['processing_value'] >\
                        learning_style['understanding_value']:
                    coordinates[cons.abbreviation_cc] = (11, 11, 11, 11)
                else:
                    coordinates[cons.abbreviation_cc] = (0, 0, 0, 0)
            elif(learning_style['processing_dimension'] == 'ref'
                 or learning_style['understanding_dimension'] == 'glo'):
                coordinates[cons.abbreviation_cc] = (11, 11, 11, 11)
            else:
                coordinates[cons.abbreviation_cc] = (0, 0, 0, 0)
        else:
            coordinate = list()
            if learning_style['processing_dimension'] == "act":
                coordinate.append(
                    learning_style['processing_value']
                    * influence[elememnt][0])
            elif learning_style['processing_dimension'] == "ref":
                coordinate.append(
                    learning_style['processing_value']
                    * influence[elememnt][1])
            if learning_style['perception_dimension'] == "sns":
                coordinate.append(
                    learning_style['perception_value']
                    * influence[elememnt][2])
            elif learning_style['perception_dimension'] == "int":
                coordinate.append(
                    learning_style['perception_value']
                    * influence[elememnt][3])
            if learning_style['input_dimension'] == "vis":
                coordinate.append(
                    learning_style['input_value']
                    * influence[elememnt][4])
            elif learning_style['input_dimension'] == "vrb":
                coordinate.append(
                    learning_style['input_value']
                    * influence[elememnt][5])
            if learning_style['understanding_dimension'] == "seq":
                coordinate.append(
                    learning_style['understanding_value']
                    * influence[elememnt][6])
            elif learning_style['understanding_dimension'] == "glo":
                coordinate.append(
                    learning_style['understanding_value']
                    * influence[elememnt][7])
            coordinates[elememnt] = tuple(coordinate)

    return coordinates


# Euclidean Distance Function
def distance(xyz1, xyz2) -> float:
    if isinstance(xyz1[0], str):
        xyz1 = xyz1[1]
        xyz2 = xyz2[1]
    return math.dist(xyz1, xyz2)


def get_learning_style( learning_style):
   
    result = {}

    str_processing = learning_style.get('processing_dimension')
    value_processing = learning_style.get('processing_value')    
    result[str_processing] = value_processing

    str_perception = learning_style.get('perception_dimension')
    value_perception = learning_style.get('perception_value')    
    result[str_perception] = value_perception


    str_input = learning_style.get('input_dimension')
    value_input = learning_style.get('input_value')    
    result[str_input] = value_input

    str_understanding = learning_style.get('understanding_dimension')
    value_understanding = learning_style.get('understanding_value')    
    result[str_understanding] = value_understanding

    for key, value in dict(result).items():
        if value == None:
            del result[key]

    #print("\nnew_learning_style__LS",learning_style )        
    #print("\nnew_Result__LS",result )
    return result     

def get_list_learning_element(learning_elements):

    classification_learning_element = []    
    lz_is_present = False
    lz_element = ''
    
    for le in learning_elements:   
        
        if le['classification']=='KÜ':
            classification_learning_element.insert(0,le['classification'])
        elif  le['classification']=='LZ':
            lz_is_present = True
            lz_element = le['classification']
        else:    
            classification_learning_element.append(le['classification'])

    if(lz_is_present):
        classification_learning_element.append(lz_element)       
    
    return classification_learning_element   


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
    # this function may not be necessary
   
    list_is_correct = []

    for iterator in input_learning_style:

        condition1 = (iterator == 'act' or iterator == 'ref')
        condition2 = (iterator == 'sns' or iterator == 'int')
        condition3 = (iterator == 'vis' or iterator == 'vrb')
        condition4 = (iterator == 'seq' or iterator == 'glo')
        
        if(condition1 or condition2 or condition3 or condition4):
            list_is_correct.append(True)        

    temp = [True, True, True, True]
    if(list_is_correct != temp):
        return True

    return False