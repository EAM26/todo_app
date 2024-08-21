import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state['new_todo']
    todos.append(todo.strip() + "\n")
    functions.write_todos(todos)
    print(todo)


st.title("My Todo App")
st.subheader("This is my todo-app")
st.write("This app is to build increase your productivity")

for todo in todos:
    st.checkbox(label=todo)


st.text_input(label=" ", placeholder="Add a new todo...",
              on_change=add_todo, key='new_todo')
