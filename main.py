# from functions import get_todo, write_todo
import functions
import time

now = time.strftime("%b %d, %Y %H:%EM:%S")
print("It is", now)
while True:
    user_input = input("Type add, show , edit, complete and exit: ")

    if user_input.startswith('add'):

        todos = functions.get_todo()

        user_input = user_input[4:] + "\n"
        todos.append(user_input)

        functions.write_todo(todos)

    elif user_input.startswith('show'):
        todos = functions.get_todo()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}-{item}")

    elif user_input.startswith('edit'):
        try:
            todos = functions.get_todo()

            number = int(user_input[5:])
            todos[number - 1] = input("Enter the new todo") + "\n"

            functions.write_todo(todos)

            print(f"you todo was changed to{todos}")
        except ValueError:
            print("You have entered a invalid command")
            continue
    elif user_input.startswith('complete'):
        try:
            todos = functions.get_todo()

            number = int(user_input[9:])

            todos.pop(number - 1)

            functions.write_todo(todos)
        except IndexError:
            print("There is no item with that number.")
            continue
    elif user_input.startswith('exit'):
        break

    else:
        print("You have entered a invalid command")


