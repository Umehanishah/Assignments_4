import random

NUM_SIDES = 6

def roll_dice():
   
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)
    total: int = die1 + die2
    print(f"🎯 You rolled: 🎲 {die1} + 🎲 {die2} = 💥 {total}")

def main():
    print("🎉 Welcome to the Dice Simulator!\n")
    
    die1: int = 10  # This variable is local to main()
    print("🔍 die1 in main() starts as: " + str(die1) + "\n")

  
    print("🔁 Rolling dice 3 times...\n")
    roll_dice()
    roll_dice()
    roll_dice()

    
    print("\n📌 die1 in main() after rolling dice is still: " + str(die1))
    print("\n🎲 Thanks for playing!")


if __name__ == '__main__':
    main()
