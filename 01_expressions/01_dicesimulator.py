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
    margin: 10px 0;
}
.dice {
    font-size: 4rem;
    animation: shake 0.5s;
}
@keyframes shake {
    0% { transform: rotate(0deg); }
    25% { transform: rotate(-15deg); }
    50% { transform: rotate(0deg); }
    75% { transform: rotate(15deg); }
    100% { transform: rotate(0deg); }
}
.roll-container {
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 15px;
    margin-bottom: 15px;
}
.scope-demo {
    background-color: #f8f9fa;
    padding: 15px;
    border-radius: 8px;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# Constants
NUM_SIDES = 6
DICE_FACES = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]

def show_dice(die1=None, die2=None):
    """Display two dice with optional values"""
    st.markdown(f"""
    <div class="dice-container">
        <div class="dice">{DICE_FACES[die1-1] if die1 else "🎲"}</div>
        <div class="dice">{DICE_FACES[die2-1] if die2 else "🎲"}</div>
    </div>
    """, unsafe_allow_html=True)

def roll_dice_pair():
    """Roll two dice and return their values"""
    # Show rolling animation
    show_dice()
    st.session_state.rolling = True
    
    # Generate random values after delay
    time.sleep(1)
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    
    # Show final dice faces
    show_dice(die1, die2)
    st.session_state.rolling = False
    
    # Display results
    total = die1 + die2
    st.write(f"**Roll result:** {die1} + {die2} = **{total}**")
    return die1, die2

def main():
    st.title("Dice Roller: Variable Scope Demo")
    
    # Variable in main() scope
    die1_main = 10
    st.markdown("""
    <div class="scope-demo">
        <h4>🔍 Variable Scope Demonstration</h4>
        <p>This shows how <code>die1_main</code> in main() scope remains unchanged while the dice rolls produce different values.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write(f"Variable in main() scope: `die1_main = {die1_main}`")
    
    if 'roll_count' not in st.session_state:
        st.session_state.roll_count = 0
    
    if st.button("🎲 Roll Two Dice", type="primary"):
        if st.session_state.roll_count < 3:
            with st.container():
                st.markdown(f"### Roll #{st.session_state.roll_count + 1}")
                with st.spinner("Rolling..."):
                    roll1, roll2 = roll_dice_pair()
                    st.write(f"Roll values stored in local variables: die1={roll1}, die2={roll2}")
                    st.session_state.roll_count += 1
        else:
            st.warning("You've already rolled 3 times!")

    st.write(f"`die1_main` in main() scope remains: {die1_main}")
    st.caption("Notice how this variable doesn't change despite the dice rolls")

if __name__ == '__main__':
    main()