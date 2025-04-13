def main():
    print("🔢 Welcome to the Power Calculator!")

    num: float = float(input("📥 Type a number: "))

    print("What would you like to calculate?")
    print("1️⃣ Square")
    print("2️⃣ Cube")
    choice = input("👉 Enter 1 or 2: ")

    if choice == "1":
        result = num ** 2
        print(f"🧮 {num} squared is {result}")
    elif choice == "2":
        result = num ** 3
        print(f"🧮 {num} cubed is {result}")
    else:
        print("⚠️ Invalid choice. Please enter 1 or 2.")

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
