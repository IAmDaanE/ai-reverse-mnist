import math

def array_to_cords(number_input):
    y = math.floor(number_input / 28)
    x = number_input - y * 28
    return x, y

def normalize_array(array):
    max_value = max(array)
    returned_array = []
    for value in array:
        returned_array.append(value / max_value)
    return returned_array