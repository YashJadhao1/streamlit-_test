import streamlit as st

def main():
    st.title('Blood Sugar Level Checker')

    # Sidebar for user input
    st.sidebar.header('Enter Blood Sugar Level')
    sugar_level = st.sidebar.number_input('Enter Blood Sugar Level', min_value=0.0, format="%.1f")

    if st.sidebar.button('Check'):
        # Display results based on sugar level
        display_result(sugar_level)

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
