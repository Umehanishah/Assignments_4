import streamlit as st # type: ignore
import math

def main():
    st.title("📐 Right Triangle Hypotenuse Calculator")
    st.markdown("Use the **Pythagorean Theorem**: _c² = a² + b²_")

    # User input for side AB and AC
    side_ab = st.number_input("📏 Enter length of side AB (perpendicular):", min_value=0.0, step=0.1, format="%.2f")
    side_ac = st.number_input("📏 Enter length of side AC (base):", min_value=0.0, step=0.1, format="%.2f")

    if st.button("🧮 Calculate Hypotenuse"):
        hypotenuse = math.sqrt(side_ab**2 + side_ac**2)
        st.success(f"✅ The length of side BC (the hypotenuse) is: **{hypotenuse:.2f}** units")

        # Optional diagram representation
        st.markdown("### 🧠 Formula Used:")
        st.latex(r"BC = \sqrt{AB^2 + AC^2}")
        st.write(f"➡️ √({side_ab}² + {side_ac}²) = {hypotenuse:.2f}")

if __name__ == '__main__':
    main()
