import streamlit as st

def main():
    st.title('Blood Pressure Checker')

    st.subheader('Enter Blood Pressure Values')
    systolic = st.number_input('Enter Systolic (mmHg)', min_value=0, format='%d')
    diastolic = st.number_input('Enter Diastolic (mmHg)', min_value=0, format='%d')

    if st.button('Check BP'):
        check_bp(systolic, diastolic)

def check_bp(systolic, diastolic):
    st.subheader('Result')
    if systolic < 90 or diastolic < 60:
        st.write('Low Blood Pressure')
    elif 90 <= systolic <= 120 and 60 <= diastolic <= 80:
        st.write('Normal Blood Pressure')
    elif 120 < systolic <= 140 or 80 < diastolic <= 90:
        st.write('Prehypertension')
    elif systolic > 140 or diastolic > 90:
        st.write('Hypertension')
    else:
        st.write('Invalid Input')

if __name__ == '__main__':
    main()
