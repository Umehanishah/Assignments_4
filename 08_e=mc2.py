def main():
    # Speed of light in meters per second
    C = 299792458  # m/s

    # Prompt the user to enter mass in kilograms
    mass_in_kg = float(input("💡 Enter kilos of mass: "))

    # Calculate energy using the formula E = m * C^2
    energy_in_joules = mass_in_kg * (C ** 2)

    # Display the results with icons and attractive look
    print("\n🌟 e = m * C^2...")
    print(f"📏 m = {mass_in_kg} kg")
    print(f"⚡ C = {C} m/s")
    print(f"💥 {energy_in_joules} joules of energy!\n")

# This line ensures the main() function is called when the script is executed
if __name__ == '__main__':
    main()
