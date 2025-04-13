import streamlit as st  # type: ignore

def main():
    st.title("📐 Triangle Perimeter Calculator")

    st.write("Enter the lengths of the three sides of the triangle:")

    side1 = st.number_input("Length of side 1:", min_value=0.0, format="%.2f")
    side2 = st.number_input("Length of side 2:", min_value=0.0, format="%.2f")
    side3 = st.number_input("Length of side 3:", min_value=0.0, format="%.2f")

    if st.button("Calculate Perimeter"):
        perimeter = side1 + side2 + side3
        st.success(f"📏 The perimeter of the triangle is: {perimeter:.2f}")

if __name__ == '__main__':
    main()
