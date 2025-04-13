import streamlit as st # type: ignore

def main():
    st.title("🔢 Power Calculator")
    
    num = st.number_input("📥 Enter a number:", format="%.2f")
    operation = st.radio("What would you like to calculate?", ["Square", "Cube"])

    if st.button("Calculate"):
        if operation == "Square":
            result = num ** 2
            st.success(f"🧮 {num} squared is {result:.2f}")
        else:
            result = num ** 3
            st.success(f"🧮 {num} cubed is {result:.2f}")

if __name__ == '__main__':
    main()
