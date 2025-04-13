import streamlit as st # type: ignore

def main():
    st.title("🌡️🔥❄️ Temperature Converter ❄️🔥🌡️")
    st.write("Choose the conversion you want to perform:")

    conversion = st.selectbox(
        "Select conversion type:",
        (
            "Fahrenheit ➡️ Celsius",
            "Celsius ➡️ Fahrenheit",
            "Celsius ➡️ Kelvin"
        )
    )

    temp_input = st.number_input("Enter the temperature value:", format="%.2f")

    if st.button("Convert"):
        if conversion == "Fahrenheit ➡️ Celsius":
            celsius = (temp_input - 32) * 5.0 / 9.0
            st.success(f"🔥 {temp_input}°F = {celsius:.2f}°C ❄️")

        elif conversion == "Celsius ➡️ Fahrenheit":
            fahrenheit = (temp_input * 9.0 / 5.0) + 32
            st.success(f"❄️ {temp_input}°C = {fahrenheit:.2f}°F 🔥")

        elif conversion == "Celsius ➡️ Kelvin":
            kelvin = temp_input + 273.15
            st.success(f"❄️ {temp_input}°C = {kelvin:.2f}K 🌌")

    st.write("🌍 Thank you for using the Temperature Converter! Stay cozy! 🧣🧤")

if __name__ == '__main__':
    main()
