# app.py
import streamlit as st
import pandas as pd

def main():
    st.title("Interactive Data Presentation with Streamlit")

    # Add a text input widget
    user_input = st.text_input("Enter your name", "John Doe")
    
    # Display the input value
    st.write("Hello,", user_input)

    # Create some sample data
    data = {
        'Name': ['John', 'Jane', 'Alice', 'Bob'],
        'Age': [25, 30, 35, 40],
        'Location': ['New York', 'London', 'Paris', 'Tokyo']
    }
    df = pd.DataFrame(data)

    # Display the data as a table
    st.write("\nSample Data:")
    st.dataframe(df)

if __name__ == "__main__":
    main()

