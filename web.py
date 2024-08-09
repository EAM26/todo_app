import streamlit as st
import functions


def add_todo():
    todo = st.session_state['new_todo']
    todos = functions.get_todos()
    todos.append(todo.title() + '\n')
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")

todos = functions.get_todos()
for todo in todos:
    checked = st.checkbox(todo)
    if checked:
        todos = functions.get_todos()
        todos.remove(todo)
        functions.write_todos(todos)


todo = st.text_input(label="", placeholder="Enter your todo",
                     value="", on_change=add_todo,
                     key='new_todo')

print(todos)
functions.write_todos(todos)
