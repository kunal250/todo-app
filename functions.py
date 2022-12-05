FILEPATH = "todos.txt"


def get_todo(filepath=FILEPATH):
    """ Read item from the text file.
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todo(todos_arg, filepath=FILEPATH):
    """" Write the todo item in the text file.
    """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


