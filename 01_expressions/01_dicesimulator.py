import random
import time
import streamlit as st
from streamlit.components.v1 import html

st.title("🎲 Dice Simulator")

# Custom CSS for dice animation
st.markdown("""
<style>
.dice {
    font-size: 5rem;
    display: inline-block;
    margin: 0 15px;
    animation: shake 0.5s infinite;
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

def show_dice(values=None):
    dice_html = ""
    for i in range(3):
        if values and i < len(values):
            dice_char = "⚀⚁⚂⚃⚄⚅"[values[i]-1]
        else:
            dice_char = "🎲"  # Default dice before roll
        dice_html += f'<span class="dice" id="dice{i}">{dice_char}</span>'
    
    html(f"""
    <div style="text-align: center; margin: 30px 0;">
        {dice_html}
    </div>
    """)

def roll_dice():
    # Show rolling animation
    show_dice()
    
    # Generate random values after delay
    time.sleep(1)
    values = [random.randint(1, 6) for _ in range(3)]
    show_dice(values)
    
    # Display results
    total = sum(values)
    st.success(f"🎯 You rolled: {values[0]} + {values[1]} + {values[2]} = **{total}**")
    return total

# Main app
if st.button("🎲 Roll the Dice!", use_container_width=True):
    with st.spinner("Rolling..."):
        roll_dice()

st.markdown("---")
st.caption("Click the button above to roll three dice!")