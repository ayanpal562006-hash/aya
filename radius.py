
import streamlit as st

st.title("🎉 Simple User Info App")

st.write("This is string application--")

# User inputs
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=0, step=1)
favourite_colour = st.text_input("Enter your favourite colour:")

# Button to display result
if st.button("Submit"):
    st.success(f"Hii {name}. I can see your age {age} and your favourite colour {favourite_colour}")