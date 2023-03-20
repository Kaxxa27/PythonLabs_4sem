import re


def text_gluer_with_constants(text_list, constants_for_switch, constants_for_continue):
    i = 0
    new_list = []
    while i < len(text_list):
        check = True
        my_str = str(text_list[i])
        for const in constants_for_switch:
            if my_str.__contains__(const):
                # const есть и там и там.
                if list(constants_for_continue).__contains__(const):
                    if "A" <= str(text_list[i + 1])[0] <= "Z":
                    #if re.fullmatch(r"[A-Z]", text_list[i + 1]):
                        check = False
                    else:
                        if i == (len(text_list) - 1):
                            break
                        my_str = my_str + text_list[i + 1]
                        i += 1
        if check:
            for const in constants_for_continue:
                if my_str.__contains__(const):
                    if i == (len(text_list) - 1):
                        break
                    my_str = my_str + text_list[i + 1]
                    i += 1
        new_list.append(my_str)
        i += 1
    return new_list
