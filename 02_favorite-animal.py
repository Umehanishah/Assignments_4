import streamlit as st

def main():
    st.title("Favorite Animal App 🐾")

    animal = st.text_input("What's your favorite animal?")

    if animal:
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
        st.write(f"My favorite animal is also {animal}! {emoji}")

if __name__ == '__main__':
    main()
