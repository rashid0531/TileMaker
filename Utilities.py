import os


def format_string_to_int(input_str):
    input_values = input_str.split(',')
    for index, value in enumerate(input_values):
        input_values[index] = int(value)
    return tuple(input_values)


def check_if_valid_file(input_path):
    abs_path = os.path.abspath(input_path)
    return os.path.isfile(abs_path)


def check_if_dir_exists(input_path):
    abs_path = os.path.abspath(input_path)
    return os.path.exists(abs_path)
