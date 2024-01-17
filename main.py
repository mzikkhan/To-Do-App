## Python uses an interpreter called CPython
## You can use .sort() to sort a list

user_prompt = "Type add, show, edit, complete, or exit: "

todos = []

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()

        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                item = item.strip("\n")
                row = f"{index + 1} {item.capitalize()}"
                print(row)
        case 'edit':
            index = int(input("Enter index of todo to edit: "))
            index -= 1
            new_todo = input("Enter new todo: ")
            todos[index] = new_todo
        case 'complete':
            number = int(input("Index of the todo completed: "))
            todos.pop(number - 1)
        case 'exit':
            break

print("Bye!")