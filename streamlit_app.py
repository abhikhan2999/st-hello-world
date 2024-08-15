import streamlit as st

# Title of the app
st.title("Hello World Streamlit App")

# Display a simple message
st.write("Welcome to your first Streamlit app!")

# Add a text input for user interaction
user_input = st.text_input("Type something:")
st.write(f"You typed: {user_input}")