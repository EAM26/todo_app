import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button], [exit_button]],
                   font=('Helvetica', 20))

while True:
    event, value = window.read()
    print(event)
    print(value)

    match event:
        case 'Add':
            todos = functions.get_todos()
            todos.append(value['todo'].title() + '\n')
            functions.write_todos(todos)

        case 'Exit':
            break

        case sg.WINDOW_CLOSED:
            break

window.close()
