import functions
import FreeSimpleGUI as sg


label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
layout = [[label],
          [input_box, add_button],
          [list_box, edit_button, complete_button],
          [exit_button]]

window = sg.Window('My To-Do App',
                   layout=layout,
                   font=('Helvetica', 20))

while True:
    event, value = window.read()
    print(event)
    print(value)
    print(value['todos'])

    match event:
        case 'Add':
            todos = functions.get_todos()
            todos.append(value['todo'].title() + '\n')
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case 'Edit':
            old_value = value['todos'][0]
            todos = functions.get_todos()
            index = todos.index(old_value)
            todos[index] = value['todo'].title() + '\n'
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case 'Complete':
            todos = functions.get_todos()
            todos.remove(value['todos'][0])
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update("")

        case 'todos':
            window['todo'].update(value=value['todos'][0].strip('\n'))

        case 'Exit':
            break

        case sg.WINDOW_CLOSED:
            break

window.close()
