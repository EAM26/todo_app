import functions
import time

now = time.strftime("%d-%b-%Y  %H:%M:%S")
print(f"It's {now}")
while True:

    user_action = input("Type add, show, edit, complete or exit: ").strip()

    if user_action.startswith('add'):
        todo = user_action.replace('add', '', 1).strip()
        todos = functions.get_todos()

        todos.append(todo.title() + "\n")

        functions.write_todos(todos)

    elif user_action.startswith('show'):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1} -{item}")
    elif user_action.startswith('edit'):
        try:
            todos = functions.get_todos()

            # get index number
            todo_num = int(user_action.replace('edit', '', 1).strip()) - 1

            todos[todo_num] = input("Enter new todo: ").title() + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Invalid command")
            continue
        except IndexError:
            print("Invalid index number. Todo not added")
            continue

    elif user_action.startswith('complete'):
        try:
            todos = functions.get_todos()
            number = int(user_action.replace('complete', '', 1).strip()) - 1
            print(f"Removed: {todos.pop(number)}")

            functions.write_todos(todos)

        except ValueError:
            print("Invalid command")
            continue
        except IndexError:
            print("Invalid index number.")
            continue
    elif user_action.startswith('exit'):
        break

    else:
        print("Command not recognized.")
