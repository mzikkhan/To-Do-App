## Python uses an interpreter called CPython
## You can use .sort() to sort a list

user_prompt = "Type add, show, edit, complete, or exit: "

todos = []

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    if 'add' in user_action:
        todo = user_action[4:] + "\n"

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'show' in user_action:
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1} {item.capitalize()}"
            print(row)

    elif 'edit' in user_action:
        try:
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            index = int(user_action[5])
            index -= 1
            new_todo = user_action[7:]
            todos[index] = new_todo + "\n"

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Command is not valid")
            continue

    elif 'complete' in user_action:
        try: # try-except blocks only catch exceptions, not syntax errors
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            number = int(user_action[9:])
            todos.pop(number - 1)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        except IndexError:
            print("There is no number like that.")

    else:
        break

print("Bye!")