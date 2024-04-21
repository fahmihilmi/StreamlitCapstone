# app.py
import streamlit as st
import pandas as pd

def main():
    st.title("Data Presentation with Streamlit")

    # Create some sample data
    data = {
        'Name': ['John', 'Jane', 'Alice', 'Bob'],
        'Age': [25, 30, 35, 40],
        'Location': ['New York', 'London', 'Paris', 'Tokyo']
    }
    df = pd.DataFrame(data)

    # Display the data as a table
    st.write("Sample Data:")
    st.dataframe(df)

if __name__ == "__main__":
    main()

