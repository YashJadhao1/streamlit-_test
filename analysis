import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def main():
    st.title('Blood Pressure Checker')

    # Sidebar for user input
    st.sidebar.header('Enter Blood Pressure Data')
    date = st.sidebar.date_input('Date', datetime.today())
    systolic = st.sidebar.number_input('Systolic BP', min_value=0)
    diastolic = st.sidebar.number_input('Diastolic BP', min_value=0)

    if st.sidebar.button('Add Data'):
        # Append data to CSV file (you can replace this with a database)
        add_data(date, systolic, diastolic)

    # Load data from CSV file (you can replace this with a database query)
    bp_data = load_data()

    if not bp_data.empty:
        st.subheader('Recent Blood Pressure Data')
        st.write(bp_data)

        # Calculate averages
        average_systolic = bp_data['Systolic'].mean()
        average_diastolic = bp_data['Diastolic'].mean()
        st.write(f'Average Systolic BP: {average_systolic}')
        st.write(f'Average Diastolic BP: {average_diastolic}')

        # Plotting using Matplotlib
        plot_data(bp_data)

def add_data(date, systolic, diastolic):
    # Create or load CSV file to store data (you can replace this with a database)
    try:
        bp_data = pd.read_csv('bp_data.csv')
    except FileNotFoundError:
        bp_data = pd.DataFrame(columns=['Date', 'Systolic', 'Diastolic'])

    new_data = pd.DataFrame({'Date': [date], 'Systolic': [systolic], 'Diastolic': [diastolic]})
    bp_data = pd.concat([bp_data, new_data], ignore_index=True)

    bp_data.to_csv('bp_data.csv', index=False)

def load_data():
    try:
        bp_data = pd.read_csv('bp_data.csv')
        bp_data['Date'] = pd.to_datetime(bp_data['Date'])  # Convert date column to datetime
        return bp_data
    except FileNotFoundError:
        return pd.DataFrame()

def plot_data(bp_data):
    plt.figure(figsize=(10, 6))

    plt.plot(bp_data['Date'], bp_data['Systolic'], marker='o', linestyle='-', color='b', label='Systolic')
    plt.plot(bp_data['Date'], bp_data['Diastolic'], marker='o', linestyle='-', color='g', label='Diastolic')

    plt.title('Blood Pressure Over Time')
    plt.xlabel('Date')
    plt.ylabel('Blood Pressure')
    plt.legend()

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)

    plt.tight_layout()
    st.pyplot(plt)

if __name__ == '__main__':
    main()
