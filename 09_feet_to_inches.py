import streamlit as st

# Conversion factors
INCHES_IN_FOOT = 12
METERS_IN_FOOT = 0.3048
YARDS_IN_FOOT = 0.333333

def convert_units(value, from_unit, to_unit):
    """Convert between different units."""
    if from_unit == "feet" and to_unit == "inches":
        return value * INCHES_IN_FOOT
    elif from_unit == "feet" and to_unit == "meters":
        return value * METERS_IN_FOOT
    elif from_unit == "feet" and to_unit == "yards":
        return value * YARDS_IN_FOOT
    elif from_unit == "inches" and to_unit == "feet":
        return value / INCHES_IN_FOOT
    elif from_unit == "meters" and to_unit == "feet":
        return value / METERS_IN_FOOT
    elif from_unit == "yards" and to_unit == "feet":
        return value / YARDS_IN_FOOT
    else:
        return value  # No conversion needed

def main():
    st.title("📏 Unit Converter")

    # User inputs for conversion
    value = st.number_input("🔢 Enter the value to convert:", min_value=0.0, step=0.1)
    from_unit = st.selectbox("🔄 Select the unit to convert from:", ["feet", "inches", "meters", "yards"])
    to_unit = st.selectbox("➡️ Select the unit to convert to:", ["feet", "inches", "meters", "yards"])

    # Perform conversion and display result
    if st.button("🔄 Convert"):
        converted_value = convert_units(value, from_unit, to_unit)
        st.write(f"🔸 {value} {from_unit} is equal to {converted_value} {to_unit}")

if __name__ == '__main__':
    main()
