import random
import time
import streamlit as st

# Custom CSS for dice animation
st.markdown("""
<style>
.dice-container {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin: 30px 0;
}
.dice {
    font-size: 5rem;
    animation: shake 0.5s;
}
@keyframes shake {
    0% { transform: rotate(0deg); }
    25% { transform: rotate(-15deg); }
    50% { transform: rotate(0deg); }
    75% { transform: rotate(15deg); }
    100% { transform: rotate(0deg); }
}
</style>
""", unsafe_allow_html=True)

# Constants
NUM_SIDES = 6
DICE_FACES = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]

def show_dice(die1_val=None, die2_val=None):
    """Display dice with optional values (shows rolling if None)"""
    cols = st.columns(2)
    with cols[0]:
        st.markdown(f'<div class="dice">{DICE_FACES[die1_val-1] if die1_val else "🎲"}</div>', 
                   unsafe_allow_html=True)
    with cols[1]:
        st.markdown(f'<div class="dice">{DICE_FACES[die2_val-1] if die2_val else "🎲"}</div>', 
                   unsafe_allow_html=True)

def roll_dice():
    """Simulates rolling two dice with visual animation"""
    # Show rolling animation
    show_dice()
    
    # Generate random values after delay
    time.sleep(1)
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    
    # Show final dice faces
    show_dice(die1, die2)
    
    # Display results
    total = die1 + die2
    st.success(f"🎯 Rolled: {die1} + {die2} = **{total}**")
    return die1, die2

def main():
    st.title("Dice Simulator with Scope Demo")
    
    die1_main = 10  # Local variable in main()
    st.write(f"🔍 die1 in main() starts as: {die1_main}")
    
    if st.button("🎲 Roll Dice", key="roll_button"):
        with st.spinner("Rolling..."):
            # Roll dice 3 times as per requirements
            for i in range(1, 4):
                st.subheader(f"Roll {i}")
                roll1, roll2 = roll_dice()
                st.write(f"📊 Roll {i} values - die1: {roll1}, die2: {roll2}")
                st.write("")  # Spacer
    
    st.write(f"📌 die1 in main() remains: {die1_main} (showing scope)")
    st.caption("Note how die1 in main() stays 10 while the rolled dice show different values")

if __name__ == '__main__':
    main()