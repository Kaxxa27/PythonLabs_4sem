import pathlib

from Task2.Constants.constants import STORAGE_PATH
import json


def create_filename(filename):
    return STORAGE_PATH / filename


def save_to_file(filename, data):
    with open(f"{filename}", "w") as write_file:
        json.dump(data, write_file)


def load_from_file(filename):
    with open(f"{filename}", "r") as read_file:
        data = json.load(read_file)
    return data


def check_file(filename):
    return pathlib.Path.exists(STORAGE_PATH / filename)
