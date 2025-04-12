import streamlit as st  # type: ignore
from datetime import datetime
import random

def main():
    st.set_page_config(page_title="🧩 Age Riddle Quiz Game", page_icon="🧠")
    st.title("🧠 Age Riddle Quiz + 🎂 Age Calculator")

    # Age logic (invisible to the user)
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

    # Show the age riddle story to the user
    st.header("📖 Meet the Characters")
    st.markdown("""
**Anton**, **Beth**, **Chen**, **Drew**, and **Ethan** are all friends. Their ages are as follows:

- Anton is 21 years old.  
- Beth is 6 years older than Anton.  
- Chen is 20 years older than Beth.  
- Drew is as old as Chen's age plus Anton's age.  
- Ethan is the same age as Chen.
    """)

    st.markdown("---")
    st.header("🎯 Riddle Quiz Time!")

    # Quiz question pool
    question_options = [
        ("Who is the oldest?", max(character_ages, key=character_ages.get), list(character_ages.keys())),
        ("Who is the youngest?", min(character_ages, key=character_ages.get), list(character_ages.keys())),
        ("Who is older: Beth or Chen?", "Chen" if chen_age > beth_age else "Beth", ["Beth", "Chen"]),
        ("Is Drew older than Ethan?", "Yes" if drew_age > ethan_age else "No", ["Yes", "No"]),
        ("Is Anton the youngest?", "Yes" if anton_age == min(character_ages.values()) else "No", ["Yes", "No"])
    ]

    question, correct_answer, choices = random.choice(question_options)
    st.subheader(f"🧐 {question}")
    user_answer = st.selectbox("Choose your answer:", choices)

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
