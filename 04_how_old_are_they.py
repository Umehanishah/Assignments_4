import streamlit as st
from datetime import datetime
import random

def main():
    st.set_page_config(page_title="🧩 Age Riddle Quiz Game", page_icon="🧠")
    st.title("🧠 Age Riddle Quiz + 🎂 Age Calculator")

    # Static character data based on the riddle
    anton_age = 21
    beth_age = anton_age + 6
    chen_age = beth_age + 20
    drew_age = chen_age + anton_age
    ethan_age = chen_age

    character_ages = {
        "Anton": anton_age,
        "Beth": beth_age,
        "Chen": chen_age,
        "Drew": drew_age,
        "Ethan": ethan_age
    }

    st.header("📋 Character Ages")
    for name, age in character_ages.items():
        st.write(f"**{name}** is **{age}** years old.")

    st.markdown("---")
    st.header("🎯 Riddle Quiz Time!")

    # Quiz question pool
    question_options = [
        ("Who is the oldest?", max(character_ages, key=character_ages.get)),
        ("Who is the youngest?", min(character_ages, key=character_ages.get)),
        ("Who is older: Beth or Chen?", "Chen" if chen_age > beth_age else "Beth"),
        ("Is Drew older than Ethan?", "Yes" if drew_age > ethan_age else "No"),
        ("Is Anton the youngest?", "Yes" if anton_age == min(character_ages.values()) else "No")
    ]

    question, correct_answer = random.choice(question_options)
    st.subheader(f"🧐 {question}")
    user_answer = st.text_input("Your answer:")

    if st.button("✅ Submit Answer"):
        if user_answer.strip().lower() == correct_answer.lower():
            st.success("🎉 Correct!")
        else:
            st.error(f"❌ Wrong answer. The correct answer is **{correct_answer}**.")

    st.markdown("---")
    st.header("📆 Calculate Your Own Age")

    birth_date = st.date_input("📅 Select your birth date:", min_value=datetime(1900, 1, 1), max_value=datetime.today())
    if st.button("🎂 Calculate My Age"):
        today = datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        st.success(f"🎈 You are **{age}** years old!")

if __name__ == "__main__":
    main()
