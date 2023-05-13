def open_file(path, flag):
    # For reading and writing.
    # Creates a new file to write to if it doesn't find one with the specified name.
    file = open(path, flag)
    with file as file:
        content = file.read()
    return content



