import streamlit as st # type: ignore

def main():
    st.title("🧮 Simple Calculator")

   
    first_number = st.number_input("Enter the first number:", step=1.0, )
    second_number = st.number_input("Enter the second number:", step=1.0, )

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
