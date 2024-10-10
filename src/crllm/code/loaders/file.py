def file(path):
    with open(path, encoding="UTF8") as loaded_file:
        return loaded_file.read()
