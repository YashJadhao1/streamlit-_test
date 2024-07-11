import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Function to load or create the data frame
def load_data():
    try:
        df = pd.read_csv('sugar_levels.csv')
        df['Date'] = pd.to_datetime(df['Date'])  # Convert 'Date' column to datetime
    except FileNotFoundError:
        df = pd.DataFrame(columns=['Date', 'Sugar Level'])
    return df

# Function to save new sugar level data
def save_data(df):
    df.to_csv('sugar_levels.csv', index=False)

# Function to plot sugar level over time
def plot_sugar_levels(df):
    plt.figure(figsize=(10, 6))
    plt.plot(df['Date'], df['Sugar Level'], marker='o', linestyle='-', color='b')
    plt.title('Blood Sugar Levels Over Time')
    plt.xlabel('Date')
    plt.ylabel('Blood Sugar Level')
    plt.xticks(rotation=45)
    st.pyplot()

# Main function for Streamlit app
def main():
    st.title('Blood Sugar Level Checker')

    # Sidebar for user input
    st.sidebar.header('Enter Blood Sugar Level')
    sugar_level = st.sidebar.number_input('Enter Blood Sugar Level', min_value=0.0, format="%.1f")

    # Load or create data frame
    df = load_data()

    if st.sidebar.button('Check'):
        # Add new entry to the data frame
        new_entry = {'Date': datetime.now(), 'Sugar Level': sugar_level}
        df = df.append(new_entry, ignore_index=True)
        # Save updated data frame
        save_data(df)
        # Display result message
        display_result(sugar_level)

    # Display recent sugar level data
    st.subheader('Recent Sugar Level Data')
    st.write(df)

    # Plot sugar levels over time
    st.subheader('Sugar Levels Over Time')
    plot_sugar_levels(df)

def display_result(sugar_level):
    st.subheader('Result')
    if sugar_level < 70:
        st.error(f'Your blood sugar level is {sugar_level}. It is too low!')
    elif sugar_level > 140:
        st.error(f'Your blood sugar level is {sugar_level}. It is too high!')
    else:
        st.success(f'Your blood sugar level is {sugar_level}. It is within the normal range.')

if __name__ == '__main__':
    main()
