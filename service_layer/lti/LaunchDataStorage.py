dict = {}
def set_value(key, value):
    # if conflict throw exception
    if key in dict:
        raise KeyError("Key already exists")
    dict[key] = value

def get_value(key):
    return dict.get(key)