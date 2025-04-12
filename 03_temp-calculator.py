def main():
    print("🌡️🔥❄️ Welcome to the Temperature Converter! ❄️🔥🌡️")
    print("Choose the conversion you want to perform:")
    print("1️⃣ Fahrenheit ➡️ Celsius")
    print("2️⃣ Celsius ➡️ Fahrenheit")
    print("3️⃣ Celsius ➡️ Kelvin")

    choice = input("Enter the number (1/2/3) of your choice: ")

    if choice == "1":
        fahrenheit = float(input("\n🌡️ Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5.0 / 9.0
        print(f"\n🔥 Temperature: {fahrenheit}°F = {celsius:.2f}°C ❄️")

    elif choice == "2":
        celsius = float(input("\n❄️ Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9.0 / 5.0) + 32
        print(f"\n❄️ Temperature: {celsius}°C = {fahrenheit:.2f}°F 🔥")

    elif choice == "3":
        celsius = float(input("\n❄️ Enter temperature in Celsius: "))
        kelvin = celsius + 273.15
        print(f"\n❄️ Temperature: {celsius}°C = {kelvin:.2f}K 🌌")

    else:
        print("\n❌ Invalid choice. Please run the program again and select 1, 2, or 3.")

    print("\n🌍 Thank you for using the Temperature Converter! Stay cozy! 🧣🧤")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
