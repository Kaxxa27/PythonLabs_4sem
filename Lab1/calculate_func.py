import constants


def calculate_func(value1, value2, operator):
    if operator in constants.ARITHMETIC_CONSTANTS["+"]:
        return value1 + value2
    if operator in constants.ARITHMETIC_CONSTANTS["-"]:
        return value1 - value2
    if operator in constants.ARITHMETIC_CONSTANTS["/"]:
        return value1 / value2
    if operator in constants.ARITHMETIC_CONSTANTS["*"]:
        return value1 * value2
    raise ValueError
