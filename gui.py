import functions
import FreeSimpleGUI as sg

sg.theme("PythonPlus")
label_clock = sg.Text("", key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button(key="Add",image_source='add.png', image_size=(25, 25),
                       mouseover_colors="Orange", tooltip="Add Todo")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button(key="Complete", image_source='complete.png',
                            mouseover_colors="Orange", tooltip="Complete Todo")
exit_button = sg.Button("Exit")
layout = [[label_clock], [label],
          [input_box, add_button],
          [list_box, edit_button, complete_button],
          [exit_button]]

window = sg.Window('My To-Do App',
                   layout=layout,
                   font=('Helvetica', 20))

while True:
    event, value = window.read(timeout=200)

    try:
        if event != sg.WINDOW_CLOSED:
            window['clock'].update(value=functions.get_time_string())
    except sg.ErrorElement as e:
        break

    match event:
        case 'Add':
            todos = functions.get_todos()
            todos.append(value['todo'].title() + '\n')
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case 'Edit':
            try:
                old_value = value['todos'][0]
                todos = functions.get_todos()
                index = todos.index(old_value)
                todos[index] = value['todo'].title() + '\n'
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select a todo first.", title="", font=('Helvetica', 20))

        case 'Complete':
            try:
                todos = functions.get_todos()
                todos.remove(value['todos'][0])
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update("")
            except IndexError:
                sg.popup("Please select a todo first.", title="", font=('Helvetica', 20))

        case 'todos':
            window['todo'].update(value=value['todos'][0].strip('\n'))

        case 'Exit':
            break

        case sg.WINDOW_CLOSED:
            break

window.close()
