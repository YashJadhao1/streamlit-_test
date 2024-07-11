import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Sample data for demonstration
data = {
    'Date': ['2024-07-01', '2024-07-02', '2024-07-03'],
    'Systolic': [120, 118, 122],
    'Diastolic': [80, 78, 82]
}

# Create a DataFrame
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Plotting function
def plot_data():
    plt.figure(figsize=(10, 6))
    plt.plot(df['Date'], df['Systolic'], marker='o', linestyle='-', color='b', label='Systolic')
    plt.plot(df['Date'], df['Diastolic'], marker='o', linestyle='-', color='g', label='Diastolic')
    plt.title('Blood Pressure Over Time')
    plt.xlabel('Date')
    plt.ylabel('Blood Pressure')
    plt.legend()
    plt.xticks(rotation=45)
    st.pyplot()

# Main Streamlit app
def main():
    st.title('Blood Pressure Checker')
    st.subheader('Blood Pressure Data')
    st.write(df)

    st.subheader('Plot')
    plot_data()

if __name__ == '__main__':
    main()
