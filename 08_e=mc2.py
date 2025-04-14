import streamlit as st # type: ignore

def main():
    # Speed of light in meters per second
    C = 299_792_458  # m/s

    st.title("💡 E = mc² Energy Calculator")

    # Get mass input from the user
    mass_in_kg = st.number_input("Enter mass (kg):", min_value=0.0, format="%.2f")

    if st.button("Calculate Energy 💥"):
        # Calculate energy
        energy_in_joules = mass_in_kg * (C ** 2)

        # Display the results
        st.markdown("### 🌟 Equation: E = m × c²")
        st.write(f"📏 Mass (m): **{mass_in_kg} kg**")
        st.write(f"⚡ Speed of Light (c): **{C} m/s**")
        st.success(f"💥 Energy: **{energy_in_joules:,.2f} joules**")

if __name__ == '__main__':
    main()
s