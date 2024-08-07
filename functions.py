FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """"
    Read s text file and return a
    list of to-do items
    """
    with open(filepath, "r") as file:
        return file.readlines()


def write_todos(content, filepath=FILEPATH):
    """
    Open or create a textfile and write
     to-do items in it
     """
    with open(filepath, 'w') as file:
        return file.writelines(content)


if __name__ == "__main__":
    print("This is the functions module running as main")
