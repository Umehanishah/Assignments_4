def main():
    # Prompt the user to enter the first number
    first_number = input("Enter the first number: ")
    first_number = int(first_number)

    # Prompt the user to enter the second number
    second_number = input("Enter the second number: ")
    second_number = int(second_number)

    # Prompt the user to choose an operation
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    choice = input("Enter the number (1/2/3/4) for the operation you want to perform: ")

    # Perform the selected operation
    if choice == "1":
        result = first_number + second_number
        print(f"\nThe sum of {first_number} and {second_number} is {result}.")
    elif choice == "2":
        result = first_number - second_number
        print(f"\nThe difference between {first_number} and {second_number} is {result}.")
    elif choice == "3":
        result = first_number * second_number
        print(f"\nThe product of {first_number} and {second_number} is {result}.")
    elif choice == "4":
        if second_number != 0:
            result = first_number / second_number
            print(f"\nThe division of {first_number} by {second_number} gives {result}.")
        else:
            print("\n❌ Error: Cannot divide by zero.")
    else:
        print("\n❌ Invalid choice. Please select a valid operation (1-4).")

# Call the main function
main()
