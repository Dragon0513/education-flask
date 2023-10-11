# The basic calculating Method for the ILS
# Every answer will affect the dimension positively or negatively by 1

# The basic learning style is calculated by the following formula:
# ils_input = if negative -> verbal, if positive -> visual
# ils_perception = if negative -> intuitive, if positive -> sensory
# ils_procession = if negative -> reflective, if positive -> active
# ils_understanding = if negative -> global, if positive -> sequential
# Answering "a" will increase the dimension by 1 (+1)
# Answering "b" will decrease the dimension by 1 (-1)

def calculate_basic_learning_style(ils_input, ils_perception,
                                   ils_procession, ils_understanding):
    print("calculate_basic_learning_strategy")
    print("ils_input: ", ils_input)
    print("ils_perception: ", ils_perception)
    print("ils_procession: ", ils_procession)
    print("ils_understanding: ", ils_understanding)

    ils_input_dim_val = calculate_ils_input(ils_input)
    ils_perception_dim_val = calculate_ils_perception(ils_perception)
    ils_procession_dim_val = calculate_ils_procession(ils_procession)
    ils_understanding_dim_val = calculate_ils_understanding(ils_understanding)

    return (ils_input_dim_val, ils_perception_dim_val, ils_procession_dim_val,
            ils_understanding_dim_val)


def calculate_ils_input(ils_input):
    ils_input_value = 0

    for value in ils_input.items():
        if value[1] == "a":
            ils_input_value = (ils_input_value + 1)
        elif value[1] == "b":
            ils_input_value = (ils_input_value - 1)

    if ils_input_value < 0:
        ils_input_dimension = "vrb"
    else:
        ils_input_dimension = "vis"

    print("ils_input_dimension: ", ils_input_dimension,
          "ils_input_value: ", abs(ils_input_value))

    return ils_input_dimension, abs(ils_input_value)


def calculate_ils_perception(ils_perception):
    ils_perception_value = 0

    for value in ils_perception.items():
        if value[1] == "a":
            ils_perception_value = (ils_perception_value + 1)
        elif value[1] == "b":
            ils_perception_value = (ils_perception_value - 1)

    if ils_perception_value < 0:
        ils_perception_dimension = "int"
    else:
        ils_perception_dimension = "sns"

    print("ils_perception_dimension: ", ils_perception_dimension,
          "ils_perception_value: ", abs(ils_perception_value))

    return ils_perception_dimension, abs(ils_perception_value)


def calculate_ils_procession(ils_procession):
    ils_procession_value = 0

    for value in ils_procession.items():
        if value[1] == "a":
            ils_procession_value = (ils_procession_value + 1)
        elif value[1] == "b":
            ils_procession_value = (ils_procession_value - 1)

    if ils_procession_value < 0:
        ils_procession_dimension = "ref"
    else:
        ils_procession_dimension = "act"

    print("ils_procession_dimension: ", ils_procession_dimension,
          "ils_procession_value: ", abs(ils_procession_value))

    return ils_procession_dimension, abs(ils_procession_value)


def calculate_ils_understanding(ils_understanding):
    ils_understanding_value = 0

    for value in ils_understanding.items():
        if value[1] == "a":
            ils_understanding_value = (ils_understanding_value + 1)
        elif value[1] == "b":
            ils_understanding_value = (ils_understanding_value - 1)

    if ils_understanding_value < 0:
        ils_understanding_dimension = "glb"
    else:
        ils_understanding_dimension = "seq"

    print("ils_understanding_dimension: ", ils_understanding_dimension,
          "ils_understanding_value: ", abs(ils_understanding_value))

    return ils_understanding_dimension, abs(ils_understanding_value)