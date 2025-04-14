import random
import streamlit as st
import time

# Constants
NUM_SIDES = 6
DICE_FACES = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]

def dice_face_html(face):
    return f'<div class="dice">{face}</div>'

def render_dice(faces):
    dice_html = ''.join([dice_face_html(DICE_FACES[face - 1]) for face in faces])
    st.markdown("""
    <style>
    .dice-container {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin: 20px 0;
    }
    .dice {
        font-size: 60px;
        animation: shake 0.4s;
    }
    @keyframes shake {
        0% { transform: rotate(0deg); }
        25% { transform: rotate(10deg); }
        50% { transform: rotate(-10deg); }
        75% { transform: rotate(10deg); }
        100% { transform: rotate(0deg); }
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown(f'<div class="dice-container">{dice_html}</div>', unsafe_allow_html=True)

def roll_dice():
    return [random.randint(1, NUM_SIDES) for _ in range(3)]

def main():
    st.title("🎲 Dice Probability Game")

    target_sum = st.slider("🎯 Select Target Sum", min_value=3, max_value=18, step=1)
    st.write(f"🎯 Your target is: **{target_sum}**")

    if st.button("🎲 Roll Dice"):
        placeholder = st.empty()

        # Dice shaking animation
        for _ in range(5):
            temp_faces = [random.randint(1, NUM_SIDES) for _ in range(3)]
            with placeholder:
                render_dice(temp_faces)
            time.sleep(0.1)

        # Final result
        final_faces = roll_dice()
        render_dice(final_faces)

        total = sum(final_faces)
        if total == target_sum:
            st.success(f"🎉 You win! The rolled sum is **{total}**.")
        else:
            st.error(f"😞 You lose! The rolled sum is **{total}**. Try again.")

if __name__ == '__main__':
    main()
