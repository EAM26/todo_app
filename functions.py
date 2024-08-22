"""
Functions belonging to the 'to do app' in gui.py
"""

from datetime import datetime


# File functions: read and write
FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """"
    Reads text file and return a
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


#  Time functions:
def get_time_string():
    """"
    Get date and time and return as string
    """
    now = datetime.now()
    return datetime.strftime(now, "%b %d, %Y  %H:%M:%S")


if __name__ == "__main__":
    print("This is the functions module running as main")


