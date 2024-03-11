import numpy as np

from errors import errors as err
from utils import constants as cons

from ..utils import rng


def delete_probability(matrix, index):
    """Delete a probability by deleting the row and
    the column of a matrix
    """
    # Delete column:
    matrix = np.delete(matrix, index, axis=1)

    # Delete row:
    matrix = np.delete(matrix, index, axis=0)
    return matrix


def normalize_matrix(matrix):
    """Normalise the whole matrix that each row sum up to 1"""
    normalized_matrix = matrix / np.sum(matrix, axis=1, keepdims=True)
    return normalized_matrix


def normalize_row(row):
    """Normalise a single row"""
    row = [float(i) / sum(row) for i in row]
    return row


def check_probability_matrix(les_len, final_prob):
    """Check if the probability matrix has the correct shape"""
    tshape = (les_len, les_len)
    if tshape != final_prob.shape:
        print("Something went wrong!")
        return False
    else:
        return True


def get_startnode(probability, les):
    """Calculates the start node of the learning path"""
    # LEs and their initial probabilities:
    # prob[0] == kurzuebersicht
    # prob[1] == lernziele
    # prob[2] == manuskript
    # prob[3] == quiz
    # prob[4] == uebung
    # prob[5] == zusammenfassung
    # prob[6] == AAM
    # prob[7] == TAM
    # prob[8] == VAM

    probability = probability[0]
    result_prob = np.zeros((11))

    if "kurzuebersicht" in les:
        result_prob[0] = probability[0]
    if "lernziele" in les:
        result_prob[1] = probability[1]
    if "manuskript_ek" in les:
        result_prob[2] = probability[2]
    if "manuskript_ab" in les:
        result_prob[3] = probability[2]
    if "manuskript_be" in les:
        result_prob[4] = probability[2]
    if "quiz_rq" in les:
        result_prob[5] = probability[3]
    if "quiz_se" in les:
        result_prob[6] = probability[3]
    if "uebung" in les:
        result_prob[7] = probability[4]
    if "zusammenfassung" in les:
        result_prob[8] = probability[5]
    if "zusatzmaterial_textuell" in les:
        result_prob[9] = probability[7]
    if "animation" in les:
        le_weight = [0.75, 0.25]
        le_temp = [probability[8], probability[6]]
        result_prob[10] = np.average(le_temp, weights=le_weight)
    # prob[0] == kurzuebersicht
    # prob[1] == lernziele
    # prob[2] == manuskript_ek
    # prob[3] == manuskript_ab
    # prob[4] == manuskript_be
    # prob[5] == quiz_rq
    # prob[6] == quiz_se
    # prob[7] == uebung
    # prob[8] == zusammenfassung
    # prob[9] == zusatzmaterial_textuell
    # prob[10] == animation

    result_prob = result_prob[np.nonzero(result_prob)]

    if len(result_prob) != len(les):
        print(
            "Something went wrong at getting probabilities "
            "for start node! (Function: get_startnode())"
        )

    # Normalize list:
    result_prob = normalize_row(result_prob)

    # Get start node:
    # start_le = np.random.choice(les, p=result_prob)
    start_le = rng.choice(les, p=result_prob)

    return start_le


def get_probability_rows(probability, les, le_weight):
    """Calculates the rows of the probability matrix"""
    final_prob = []

    # Get rows:
    if cons.name_kü in les:
        final_prob.append(probability[0])
    if cons.name_lz in les:
        final_prob.append(probability[1])
    if cons.name_ek in les:
        final_prob.append(probability[2])
    if cons.name_ab in les:
        final_prob.append(probability[2])
    if cons.name_be in les:
        final_prob.append(probability[2])
    if cons.name_rq in les:
        final_prob.append(probability[3])
    if cons.name_se in les:
        final_prob.append(probability[3])
    if cons.name_üb in les:
        final_prob.append(probability[4])
    if cons.name_zf in les:
        final_prob.append(probability[5])
    if cons.name_zl in les:
        final_prob.append(probability[7])
    if cons.name_an in les:
        average_temp = []
        for j in range(len(probability[8])):
            le_t = [probability[8][j], probability[6][j]]
            average_temp.append(np.average(le_t, weights=le_weight))
        final_prob.append(np.asarray(average_temp))
    return final_prob


def set_le_flags(les, final_prob):
    """Sets the learning elements flags for MS, QU, AN to true
    if they are available.
    """
    flag_manuskript = False
    flag_quiz = False
    flag_animation = False
    counter = 0
    if "kurzuebersicht" not in les:
        final_prob = np.delete(final_prob, 0, axis=1)
        counter += 1
    if "lernziele" not in les:
        final_prob = np.delete(final_prob, 1 - counter, axis=1)
        counter += 1
    if "manuskript_ek" not in les:
        if "manuskript_ab" not in les:
            if "manuskript_be" not in les:
                final_prob = np.delete(final_prob, 2 - counter, axis=1)
                counter += 1
            else:
                flag_manuskript = True
        else:
            flag_manuskript = True
    else:
        flag_manuskript = True
    if "quiz_rq" not in les:
        if "quiz_se" not in les:
            final_prob = np.delete(final_prob, 3 - counter, axis=1)
            counter += 1
        else:
            flag_quiz = True
    else:
        flag_quiz = True
    if "uebung" not in les:
        final_prob = np.delete(final_prob, 4 - counter, axis=1)
    if "zusammenfassung" not in les:
        final_prob = np.delete(final_prob, 5 - counter, axis=1)
        counter += 1
    if "animation" not in les:
        final_prob = np.delete(final_prob, 6 - counter, axis=1)
        counter += 1
    if "zusatzmaterial_textuell" not in les:
        final_prob = np.delete(final_prob, 7 - counter, axis=1)
        counter += 1
    if "animation" not in les:
        final_prob = np.delete(final_prob, 8 - counter, axis=1)
        counter += 1
    else:
        flag_animation = True
    return flag_manuskript, flag_quiz, flag_animation, final_prob


def add_ms_probs(flag_manuskript, final_prob, les):
    """Adds rows of manuscript probabilities if needed"""
    counter_ms = 0
    if flag_manuskript:
        if "manuskript_ek" in les:
            counter_ms += 1
        if "manuskript_ab" in les:
            counter_ms += 1
        if "manuskript_be" in les:
            counter_ms += 1

        # Insert missing probabilities for manuscript:
        if counter_ms > 1:
            duplicate_column = final_prob[:, counter_ms]
            for _i in range(counter_ms - 1):
                final_prob = np.insert(
                    final_prob, counter_ms + 1, duplicate_column, axis=1
                )
    return final_prob


def add_qu_probs(flag_quiz, final_prob, les):
    """Adds rows of quiz probabilities if needed"""
    if flag_quiz:
        counter_qu = 0
        if "quiz_rq" in les:
            counter_qu += 1

        if "quiz_se" in les:
            counter_qu += 1

        # Insert missing probabilities for quiz:
        if counter_qu == 2:
            duplicate_column = final_prob[:, counter_qu]
            final_prob = np.insert(final_prob, counter_qu + 1, duplicate_column, axis=1)
    return final_prob


def add_animation_probs(flag_animation, final_prob, les, le_weight):
    """Adds rows of animation probabilities if needed"""
    if flag_animation:  # weighted average of AAM and VAM
        # Get probs of AAM and VAM
        colum_sum = []
        if cons.name_zl in les:
            w = 3
        else:
            w = 2
        for i in range(len(final_prob)):
            le_t = [final_prob[i][-1], final_prob[i][-w]]
            colum_sum.append([np.average(le_t, weights=le_weight)])

        # Delete probs of AAM and VAM in final_prob
        final_prob = np.delete(final_prob, -1, axis=1)
        final_prob = np.delete(final_prob, ((w - 1) * (-1)), axis=1)

        # Add column of animation at the end of final_prob:
        final_prob = np.append(final_prob, colum_sum, axis=1)
    return final_prob


def get_probability_columns(les, le_weight, final_prob):
    """Calculates the columns of the probability matrix.
    Deletes columns if needed.
    """
    final_prob = np.asarray(final_prob)

    flag_manuskript, flag_quiz, flag_animation, final_prob = set_le_flags(
        les, final_prob
    )

    # Adapt probabilities for animation:
    final_prob = add_animation_probs(flag_animation, final_prob, les, le_weight)

    # Adapt probabilities for manuskript:
    final_prob = add_ms_probs(flag_manuskript, final_prob, les)

    # Adapt probabilities for quiz:
    final_prob = add_qu_probs(flag_quiz, final_prob, les)
    return final_prob


def get_probability_matrix(probability, les):
    """Main function for setting up the probability matrix"""
    le_weight = [0.75, 0.25]
    les_len = len(les)

    # Transform probability matrix:
    final_prob = get_probability_rows(probability, les, le_weight)

    # Get columns:
    final_prob = get_probability_columns(les, le_weight, final_prob)

    # Check probability matrix:
    if not check_probability_matrix(les_len, final_prob):
        errmsg = "Error in matrix generation"
        raise err.ErrorException(message=errmsg)

    return final_prob


def get_nextnodes(probability, les, start_node):
    """Calculates all further nodes with a given start node"""
    learningpath = [start_node]

    final_prob = get_probability_matrix(probability, les)

    # Normalize probabilities:
    probs = normalize_matrix(final_prob)

    # Calculate next nodes:
    if len(les) == 1:
        learningpath.append(les)
    else:
        for _i in range(len(les) - 1):
            curr_le_index = les.index(start_node)
            temp_prob = probs[curr_le_index]

            # Delete probability of current start node:
            temp_prob = temp_prob.tolist()
            temp_prob.pop(curr_le_index)
            temp_prob = np.asarray(temp_prob)
            temp_prob = normalize_row(temp_prob)

            # Delete current start node from les:
            les.pop(curr_le_index)

            # Get next learning element:
            # nextn = np.random.choice(les, p=temp_prob)
            nextn = rng.choice(les, p=temp_prob)
            learningpath.append(nextn)

            # Delete probabilities for current start node:
            probs = delete_probability(probs, curr_le_index)

            # Set new start node:
            start_node = nextn
    return learningpath
