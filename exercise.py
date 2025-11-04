import streamlit as st
from time import sleep
#Title
st.title("Math Score Prediction")
st.header('Data Collection Section')

if "submitted" not in st.session_state:
    st.session_state.submitted = False
with st.form(key="cheryl_form", enter_to_submit=False, border=True, width= "stretch", height="content", clear_on_submit=False):
    # Text Input
    name = st.text_input(label="Enter your name:", placeholder="Nana Kwame")

    # Slider
    age= st.slider("Enter your age:", 15, 30)
    
    #Selectbox
    address = st.selectbox("Where do you stay:", [ 'Ayeduase', 'New Site', 'Boadi', 'Appiadu', 'On-campus', 'Kotei'])

    #Submit Button
    if st.form_submit_button("Submit"):
        st.session_state.submitted = True

    data = {"name": name, "age": age, "address": address}

if st.session_state.submitted:
    progress_message = "Submitting Data. Please wait."
    progress_bar = st.progress(0, text=progress_message)
    for percent_complete in range(100):
        sleep(0.02)  # Simulate a long-running process
        progress_bar.progress(percent_complete + 1, text=progress_message)
    progress_bar.empty()
    st.balloons()
    st.toast("Form Submitted Successfully!", icon="✅")
    st.write("Data Submitted Successfully!")

    st.header('Image Upload Section')
    uploaded_file = st.file_uploader("Upload an image of your handwritten math score:", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
        st.snow()

        st.header('Prediction Section')

        gender = st.radio('Enter your gender:',['Male', 'Female'])
        st.write(f'You selected: {gender}')

        education_level = st.selectbox("Select your parent education level:", ['High School(completed)', 'Undergraduate', 'Graduate', 'Postgraduate'])

        completion_status = st.selectbox("Did student complete a test prep course:", ['Completed', 'Not Completed'])

        if st.form_submit_button("Make Prediction"):
            st.session_state.prediction = True

         
    #st.success("Form Submitted Successfully!")
   # st.write(f"Name: {name}")
    #st.write(f"Age: {age}")
   # st.write(f"Address: {address}")

