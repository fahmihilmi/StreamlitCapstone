# app.py
import streamlit as st

def main():
    st.title("Simple Streamlit App")
    
    # Add a text input widget
    user_input = st.text_input("Enter your name", "John Doe")
    
    # Display the input value
    st.write("Hello,", user_input)

if __name__ == "__main__":
    main()
