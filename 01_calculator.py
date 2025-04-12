import streamlit as st # type: ignore

def main():
    st.title("🧮 Simple Calculator")

    # Remove .00 by converting to integers when possible
    first_number = st.number_input("Enter the first number:", step=1.0)
    if first_number.is_integer():
        first_number = int(first_number)  # Convert to integer to remove ".00"

    second_number = st.number_input("Enter the second number:", step=1.0)
    if second_number.is_integer():
        second_number = int(second_number)  # Convert to integer to remove ".00"
    
    # Display a numeric keypad with + and - buttons
    st.subheader("Choose a number from 0-9:")
    
    col1, col2, col3 = st.columns(3)

    with col1:
        number = st.button("0")
        if number:
            first_number = 0

    with col2:
        number = st.button("1")
        if number:
            first_number = 1

    with col3:
        number = st.button("2")
        if number:
            first_number = 2

    col1, col2, col3 = st.columns(3)

    with col1:
        number = st.button("3")
        if number:
            first_number = 3

    with col2:
        number = st.button("4")
        if number:
            first_number = 4

    with col3:
        number = st.button("5")
        if number:
            first_number = 5

    col1, col2, col3 = st.columns(3)

    with col1:
        number = st.button("6")
        if number:
            first_number = 6

    with col2:
        number = st.button("7")
        if number:
            first_number = 7

    with col3:
        number = st.button("8")
        if number:
            first_number = 8

    col1, col2, col3 = st.columns(3)

    with col1:
        number = st.button("9")
        if number:
            first_number = 9

    # Operation choice
    operation = st.selectbox("Choose an operation:", 
                             ["Addition (+)", 
                              "Subtraction (-)", 
                              "Multiplication (*)", 
                              "Division (/)"])

    if st.button("Calculate"):
        if operation == "Addition (+)":
            result = first_number + second_number
            st.success(f"The sum of {first_number} and {second_number} is {result}")
        elif operation == "Subtraction (-)":
            result = first_number - second_number
            st.success(f"The difference between {first_number} and {second_number} is {result}")
        elif operation == "Multiplication (*)":
            result = first_number * second_number
            st.success(f"The product of {first_number} and {second_number} is {result}")
        elif operation == "Division (/)":
            if second_number != 0:
                result = first_number / second_number
                st.success(f"The division of {first_number} by {second_number} is {result}")
            else:
                st.error("❌ Error: Cannot divide by zero.")

# Run app
if __name__ == "__main__":
    main()
