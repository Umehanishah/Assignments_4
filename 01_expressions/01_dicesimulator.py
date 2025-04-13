import random
import time
import streamlit as st # type: ignore

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
    animation: shake 10s;
}
@keyframes shake {
    0% { transform: rotate(0deg); }
    25% { transform: rotate(-15deg); }
    50% { transform: rotate(0deg); }
    75% { transform: rotate(15deg); }
    100% { transform: rotate(0deg); }
}
.result-box {
    border: 1px solid #ccc;
    border-radius: 5px;
    padding: 10px;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

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
    """Simulates rolling three dice with visual animation"""
    # Show rolling animation
    show_dice()
    
    # Generate random values after delay
    time.sleep(1)
    dice_values = [random.randint(1, NUM_SIDES) for _ in range(3)]
    
    # Show final dice faces
    show_dice(dice_values)
    
    # Display results
    total = sum(dice_values)
    st.markdown(f"""
    <div class="result-box">
        <h3>🎯 Rolled: {dice_values[0]} + {dice_values[1]} + {dice_values[2]} = <strong>{total}</strong></h3>
    </div>
    """, unsafe_allow_html=True)
    return dice_values

def main():
    st.title("🎲 Triple Dice Simulator")
    
    die1_main = 10  # Local variable in main()
    st.write(f"🔍 Main scope variable: {die1_main}")
    
    if st.button("🎲 Roll Dices", type="primary", use_container_width=True):
        with st.spinner("Rolling all three dice..."):
            dice_results = roll_dice()
            st.write(f"📊 Dice values: {dice_results}")
    
    st.write(f"📌 die1 in main() remains: {die1_main} (showing scope)")
    st.caption("Note how the main scope variable stays constant while dice results change")

if __name__ == '__main__':
    main()