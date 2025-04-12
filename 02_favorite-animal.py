def main():
    
    animal = input("What's your favorite animal? ")

    animal_emojis = {
        "dog": "🐶",
        "cat": "🐱",
        "cow": "🐄",
        "lion": "🦁",
        "tiger": "🐯",
        "monkey": "🐵",
        "elephant": "🐘",
        "panda": "🐼",
        "rabbit": "🐰",
        "fox": "🦊",
        "bear": "🐻",
        "chicken": "🐔",
        "penguin": "🐧",
        "horse": "🐴",
        "frog": "🐸"
    }

  
    emoji = animal_emojis.get(animal.lower(), "🐾")

    print(f"\nMy favorite animal is also {animal}! {emoji}")


if __name__ == '__main__':
    main()
