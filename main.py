## Python uses an interpreter called CPython
## You can use .sort() to sort a list
## Use docstrings for every function

from functions import get_todos, write_todos
# import functions as fn, fn.get_todos()
# you can keep functions in a separate module as:
## from modules import functions as fn, fn.get_todos()

user_prompt = "Type add, show, edit, complete, or exit: "

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    if 'add' in user_action:
        todo = user_action[4:] + "\n"

        todos = get_todos('todos.txt')

        todos.append(todo)

        write_todos(todos, 'todos.txt')

    elif 'show' in user_action:
        todos = get_todos('todos.txt')

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1} {item.capitalize()}"
            print(row)

    elif 'edit' in user_action:
        try:
            todos = get_todos('todos.txt')

            index = int(user_action[5])
            index -= 1
            new_todo = user_action[7:]
            todos[index] = new_todo + "\n"

            write_todos(todos, 'todos.txt')
        except ValueError:
            print("Command is not valid")
            continue

    elif 'complete' in user_action:
        try: # try-except blocks only catch exceptions, not syntax errors
            todos = get_todos('todos.txt')

            number = int(user_action[9:])
            todos.pop(number - 1)

            write_todos(todos, 'todos.txt')
        except IndexError:
            print("There is no number like that.")

    else:
        break

print("Bye!")