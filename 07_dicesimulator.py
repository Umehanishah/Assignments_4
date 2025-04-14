import random
import streamlit as st # type: ignore

# Constants
NUM_SIDES = 6
DICE_FACES = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]

def show_dice(dice_values=None):
    """Display 3 dice in a line with optional values (shows rolling if None)"""
    dice_html = ""
    for i in range(3):
        if dice_values and i < len(dice_values):
            dice_char = DICE_FACES[dice_values[i]-1]
        else:
            dice_char = "🎲"  # Default dice before roll
        dice_html += f'<div class="dice">{dice_char}</div>'
    
    st.markdown(f"""
    <div class="dice-container">
        {dice_html}
    </div>
    """, unsafe_allow_html=True)

def roll_dice():
    """Simulates rolling three dice and returns the results"""
    # Show rolling animation
    show_dice()
    
    # Generate random values for the dice
    dice_values = [random.randint(1, NUM_SIDES) for _ in range(3)]
    
    # Show final dice faces
    show_dice(dice_values)
    
    # Return the dice results
    return dice_values

def main():
    st.title("🎲 Dice Probability Game")

    # Allow the user to select the probability target (target sum)
    target_sum = st.slider("Select Target Sum", min_value=3, max_value=18, step=1)

    st.write(f"🎯 Your target sum is: {target_sum}")
    
    # Button to roll the dice and check if user wins
    if st.button("🎲 Roll Dices", type="primary", use_container_width=True):
        dice_results = roll_dice()
        total = sum(dice_results)
        
        # Check if the sum matches the target
        if total == target_sum:
            st.success(f"🎉 You win! The rolled sum is {total}.")
        else:
            st.error(f"😞 You lose! The rolled sum is {total}. Try again.")

if __name__ == '__main__':
    main()
