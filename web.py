import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state['new_todo'].strip() + "\n"
    if todo not in todos:
        todos.append(todo)
        functions.write_todos(todos)
        st.session_state['new_todo'] = ""



st.title("My Todo App")
st.subheader("This is my todo-app")
st.write("This app is to build increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(label=todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)

        # Streamlit automatically tracks the state of the checkbox (whether it is checked or unchecked)
        # in st.session_state
        del st.session_state[todo]
        st.rerun()


st.text_input(label="Add todo", placeholder="Enter new todo .....",
              on_change=add_todo, key='new_todo', value=st.session_state.get('new-todo', ''))

st.session_state
