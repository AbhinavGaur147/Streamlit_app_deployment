import streamlit as st

# Title of the app
st.title("My First Streamlit APP Test")
st.title("Testing")

# Subheader
st.subheader("Welcome to my first Streamlit app!")

# Text
st.write("This is a simple Streamlit app to demonstrate basic features.")

# Checkbox
if st.checkbox("Show more details"):
    st.write("Here are some more details...")

# Slider
age = st.slider("Select your age", 0, 100, 25)
st.write(f"Your age is: {age}")

# Button
if st.button("Click me"):
    st.write("Button clicked!")

# Selectbox
option = st.selectbox("Choose an option", ["Option 1", "Option 2", "Option 3"])
st.write(f"You selected: {option}")

# Text input
name = st.text_input("Enter your name")
if name:
    st.write(f"Hello, {name}!")

# URL of the image
image_url = "https://www.istockphoto.com/photo/giant-panda-baby-cub-in-chengdu-area-china-gm539113690-96047311"

# Display the image
st.image(image_url, caption='Sample Image', use_column_width=True)
