import streamlit as st

# Add an icon to the app
st.set_page_config(page_title="Division with Remainder", page_icon="🔢")

# Title of the app
st.title("Division and Remainder Calculator")

# Add a friendly divider with an icon in the sidebar
st.sidebar.header("Welcome to the Division App")
st.sidebar.subheader("Calculate the result and remainder of any two integers")

# Add icons in the sidebar for a nice touch
st.sidebar.image("https://www.streamlit.io/images/brand/streamlit-logo-color.svg", width=100)

# Ask the user for input with icons for the numbers
num1 = st.number_input("Please enter an integer to be divided: 🔢", min_value=-10000, max_value=10000)
num2 = st.number_input("Please enter an integer to divide by: ➗", min_value=-10000, max_value=10000)

# Check if the second number is not zero to avoid division by zero
if num2 != 0:
    result = num1 // num2  # Integer division
    remainder = num1 % num2  # Remainder
    st.write(f"The result of this division is {result} with a remainder of {remainder} 👍")
else:
    st.error("Division by zero is not allowed! ⚠️")

# Add an icon in the footer for visual appeal
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit 🚀")
