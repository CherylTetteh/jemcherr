import streamlit as st
#Title
st.title("Welcome")
st.write("Choose an option")

# Various text elements
st.markdown('**Bold text** and *Italic text*.')
st.header('Header Example')
st.subheader('Subheader Example')
st.caption('This is a caption text.')

#input elements
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")
age = st.number_input("Enter your age:", min_value=0, max_value=120)
if age:
    st.write(f"You are {age} years old.")


# Buttons and State
if 'count' not in st.session_state:
    st.session_state.count = 0
if st.button("Add"):
    st.session_state.count += 1
if st.button("Subtract"):
    st.session_state.count -= 1
st.write('counter:', st.session_state.count)

# Selectbox and Radio Buttons
choice = st.radio('choose a dish:',['banku', 'Fufu', 'Fries'])
st.write(f'You selected: {choice}') 