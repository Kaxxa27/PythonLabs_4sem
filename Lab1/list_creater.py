import random


def create_list(len_list):
    created_list = []

    for i in range(len_list):
        created_list.append(random.randint(1, 100))
    print("FULL: " + str(created_list))
    print("EVEN: " + str(list(filter(lambda x: not int(x) % 2, created_list))))
    return created_list
