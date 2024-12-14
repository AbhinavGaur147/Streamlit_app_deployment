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
image_url = "https://media.istockphoto.com/id/1222602125/photo/mother-panda-walking-with-panda-cub.jpg?s=612x612&w=0&k=20&c=-9ulesjKZK2zvn7uBpwo6_33-3FoZcQE52FQhZiCpeM="

# Display the image
st.image(image_url, caption='Sample Image' ,use_container_width=True, clamp=True, channels='RGB', output_format='auto)
