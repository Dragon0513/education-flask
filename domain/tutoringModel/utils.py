import math

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
        if elememnt == "KÜ":
            coordinates['KÜ'] = (13, 13, 13, 13)
        elif elememnt == "EK":
            coordinates['EK'] = (12, 12, 12, 12)
        elif elememnt == "LZ":
            coordinates['LZ'] = (-12, -12, -12, -12)
        elif elememnt == "ZF":
            if(learning_style['processing_dimension'] == 'ref'
               and learning_style['understanding_dimension'] == 'seq'):
                if learning_style['processing_value'] >\
                        learning_style['understanding_value']:
                    coordinates['ZF'] = (11, 11, 11, 11)
                else:
                    coordinates['ZF'] = (0, 0, 0, 0)
            elif(learning_style['processing_dimension'] == 'ref'
                 or learning_style['understanding_dimension'] == 'glo'):
                coordinates['ZF'] = (11, 11, 11, 11)
            else:
                coordinates['ZF'] = (0, 0, 0, 0)
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
