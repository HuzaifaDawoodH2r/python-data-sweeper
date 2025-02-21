# Imports
import streamlit as st
import pandas as pd
import os
from io import BytesIO 

# Set up our App
st.set_page_config(page_title="📀 Data Sweeper", layout='wide')
st.title("🏳️‍🌈 Growth Mindset Challenge")
st.write("Embrace challenges, learn from mistakes, and unlock your potential.")

# Quotes section
st.header("💡 Today's Mindset Quote")
st.write("This is not final; failure is not fatal.")

# Challenge section
st.header("🔧 What is your challenge project?")
user_input = st.text_input("You are facing a challenge:")

# Condition
if user_input:
    st.success(f"👏🏼 You are facing '{user_input}' successfully!")
else:
    st.warning("Tell me about your challenge.")

# Reflection
st.header("📝 Reflect on your learning")
reflection = st.text_area("Write your reflection here:")

if reflection:
    st.success(f"Great in side your reflection {reflection}")

elif not reflection:
    st.info("Please enter something to reflect on.")

st.header("Achievements")

# Example achievements (You can customize these)
achievements = [
    "🏆 Completed 100+ successful web development projects.",
    "💻 Mastered HTML, CSS, TypeScript,python, and currently learning Next.js.",
    "🚀 Designed and launched multiple responsive, user-friendly web applications.",
    "🎨 Improved user experience for clients, increasing user engagement by 30%."
]

# Display each achievement
for achievement in achievements:
    st.write(achievement)