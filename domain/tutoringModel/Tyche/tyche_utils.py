import numpy as np


def delete_probability(matrix, index):
    # Delete column:
    matrix = np.delete(matrix, index, axis=1)
    # Delete row:
    matrix = np.delete(matrix, index, axis=0)
    return matrix


def normalize_matrix(matrix):
    normalized_matrix = matrix / np.sum(matrix, axis=1, keepdims=True)
    return normalized_matrix


def normalize_row(row):
    row = [float(i)/sum(row) for i in row]
    return row


def get_startnode(probability, les):
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
        temp = 0
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
    result_prob = np.delete(result_prob, np.where(result_prob == 0))

    if len(result_prob) != len(les):
        print("Something went wrong at getting probabilities "
              "for start node! (Function: get_startnode())")
    # Normalize list:
    result_prob = normalize_row(result_prob)

    # Get start node:
    start_le = np.random.choice(les, p=result_prob)
    # print("First LE:", start_le)
    return start_le


def get_nextnodes(probability, les, start_node):
    learningpath = [start_node]
    le_weight = [0.75, 0.25]
    les_len = len(les)

    # Transform probability matrix:
    final_prob = []
    # Get rows:
    if "kurzuebersicht" in les:
        final_prob.append(probability[0])
    if "lernziele" in les:
        final_prob.append(probability[1])
    if "manuskript_ek" in les:
        final_prob.append(probability[2])
    if "manuskript_ab" in les:
        final_prob.append(probability[2])
    if "manuskript_be" in les:
        final_prob.append(probability[2])
    if "quiz_rq" in les:
        final_prob.append(probability[3])
    if "quiz_se" in les:
        final_prob.append(probability[3])
    if "uebung" in les:
        final_prob.append(probability[4])
    if "zusammenfassung" in les:
        final_prob.append(probability[5])
    if "zusatzmaterial_textuell" in les:
        final_prob.append(probability[7])
    if "animation" in les:
        average_temp = []
        for j in range(len(probability[8])):
            le_t = [probability[8][j], probability[6][j]]
            average_temp.append(np.average(le_t, weights=le_weight))
        final_prob.append(np.asarray(average_temp))

    # Get columns:
    final_prob = np.asarray(final_prob)
    flag_manuskript = False
    flag_quiz = False
    flag_animation = False
    counter = 0
    if "kurzuebersicht" not in les:
        # for k in range(len(final_prob)):
        final_prob = np.delete(final_prob, 0, axis=1)
        counter = counter + 1
    if "lernziele" not in les:
        final_prob = np.delete(final_prob, 1 - counter, axis=1)
        counter = counter + 1
    if "manuskript_ek" not in les:
        if "manuskript_ab" not in les:
            if "manuskript_be" not in les:
                final_prob = np.delete(final_prob, 2 - counter, axis=1)
                counter = counter + 1
            else:
                flag_manuskript = True
        else:
            flag_manuskript = True
    else:
        flag_manuskript = True
    if "quiz_rq" not in les:
        if "quiz_se" not in les:
            final_prob = np.delete(final_prob, 3 - counter, axis=1)
            counter = counter + 1
        else:
            flag_quiz = True
    else:
        flag_quiz = True
    if "uebung" not in les:
        final_prob = np.delete(final_prob, 4 - counter, axis=1)
    if "zusammenfassung" not in les:
        final_prob = np.delete(final_prob, 5 - counter, axis=1)
        counter = counter + 1
    if "animation" not in les:
        final_prob = np.delete(final_prob, 6 - counter, axis=1)
        counter = counter + 1
    if "zusatzmaterial_textuell" not in les:
        final_prob = np.delete(final_prob, 7 - counter, axis=1)
        counter = counter + 1
    if "animation" not in les:
        final_prob = np.delete(final_prob, 8 - counter, axis=1)
        counter = counter + 1
    else:
        flag_animation = True

    if flag_animation:  # weighted average of AAM and VAM
        # Get probs of AAM and VAM
        colum_sum = []
        if "zusatzmaterial_textuell" in les:
            w = 3
        else:
            w = 2

        for i in range(len(final_prob)):
            le_t = [final_prob[i][-1], final_prob[i][-w]]
            colum_sum.append([np.average(le_t, weights=le_weight)])

        # Delete probs of AAM and VAM in final_prob
        final_prob = np.delete(final_prob, -1, axis=1)
        final_prob = np.delete(final_prob, ((w-1)*(-1)), axis=1)

        # Add column of animation at the end of final_prob:
        final_prob = np.append(final_prob, colum_sum, axis=1)
        pass

    counter_ms = 0
    index_ms1 = False
    index_ms2 = False
    index_ms3 = False
    first_ms_prob = -1
    if flag_manuskript:
        if "manuskript_ek" in les:
            counter_ms = counter_ms + 1
            index_ms1 = les.index("manuskript_ek")
            if first_ms_prob > index_ms1:
                first_ms_prob = index_ms1
        if "manuskript_ab" in les:
            counter_ms = counter_ms + 1
            index_ms2 = les.index("manuskript_ab")
            if first_ms_prob > index_ms2:
                first_ms_prob = index_ms2
        if "manuskript_be" in les:
            counter_ms = counter_ms + 1
            index_ms3 = les.index("manuskript_be")
            if first_ms_prob > index_ms3:
                first_ms_prob = index_ms3
        # Insert missing probabilities for manuskript:
        if counter_ms > 1:
            duplicate_column = final_prob[:, counter_ms]
            for i in range(counter_ms - 1):
                final_prob = np.insert(final_prob,
                                       counter_ms + 1,
                                       duplicate_column,
                                       axis=1)

    index_qu1 = False
    index_qu2 = False
    first_qu_prob = -1
    if flag_quiz:
        counter_qu = 0
        if "quiz_rq" in les:
            counter_qu = counter_qu + 1
            index_qu1 = les.index("quiz_rq")
            if first_qu_prob > index_qu1:
                first_qu_prob = index_qu1
        if "quiz_se" in les:
            counter_qu = counter_qu + 1
            index_qu2 = les.index("quiz_se")
            if first_qu_prob > index_qu2:
                first_qu_prob = index_qu2
        # Insert missing probabilities for quiz:
        if counter_qu == 2:
            duplicate_column = final_prob[:, counter_qu]
            final_prob = np.insert(final_prob,
                                   counter_qu + 1,
                                   duplicate_column,
                                   axis=1)

    # Check probability matrix:
    tshape = (les_len, les_len)
    if tshape != final_prob.shape:
        print("Something went wrong!")

    # Normalize probabilities:
    probs = normalize_matrix(final_prob)

    # Calculate next nodes:
    if len(les) == 1:
        learningpath.append(les)
    else:
        for i in range(len(les) - 1):
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
            nextn = np.random.choice(les, p=temp_prob)
            learningpath.append(nextn)

            # Delete probabilities for current start node:
            probs = delete_probability(probs, curr_le_index)
            # Set new start node:
            start_node = nextn

    return learningpath
