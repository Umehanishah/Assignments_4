import random
import streamlit as st

st.title("Dice Simulator 🎲")

NUM_SIDES = 6

def roll_dice():
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    st.write(f"🎯 You rolled: 🎲 {die1} + 🎲 {die2} = 💥 {total}")

def main():
    st.write("🎉 Welcome to the Dice Simulator!\n")
    
    die1 = 10  # This variable is local to main()
    st.write("🔍 die1 in main() starts as: " + str(die1) + "\n")

    st.write("🔁 Rolling dice 3 times...\n")
    roll_dice()
    roll_dice()
    roll_dice()

    st.write("\n📌 die1 in main() after rolling dice is still: " + str(die1))
    st.write("\n🎲 Thanks for playing!")

if __name__ == '__main__':
    main()