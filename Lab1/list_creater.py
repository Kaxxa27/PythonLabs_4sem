import random


def create_list():
    created_list = []
    len_list = int(input("Enter list length: "))
    for i in range(len_list):
        created_list.append(random.randint(1, 100))
    return created_list
