import streamlit as st
import pandas as pd
from datetime import datetime

# Set up our App with a modern design
st.set_page_config(page_title="Growth Mindset Tracker", layout='wide')

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stTitle {
        color: #2E4057;
        font-size: 3rem !important;
    }
    .quote-box {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
    }
    .challenge-box {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 20px 0;
    }
    </style>
""", unsafe_allow_html=True)

# App Header with emoji
st.title("🌟 Growth Mindset Challenge")
st.write("Embrace challenges, learn from mistakes, and unlock your potential.")

# Quotes section with better styling
st.markdown("### 💡 Today's Mindset Quote")
st.markdown("""
    <div class='quote-box'>
        "Success is not final, failure is not fatal: it is the courage to continue that counts." - Winston Churchill
    </div>
""", unsafe_allow_html=True)

# Create columns for better layout
col1, col2 = st.columns(2)

with col1:
    # Challenge section
    st.markdown("### 🔧 Your Challenge")
    user_challenge = st.text_input("What challenge are you facing today?")
    
    if user_challenge:
        st.success(f"👏 You're bravely facing: '{user_challenge}'")
    else:
        st.info("Share your challenge with us...")

with col2:
    # Reflection section
    st.markdown("### 📝 Daily Reflection")
    reflection = st.text_area("Reflect on your learning journey:")
    
    if reflection:
        st.success("Thank you for sharing your thoughts!")
    elif not reflection:
        st.info("Take a moment to reflect...")

# Achievements section with better styling
st.markdown("### 🏆 Your Achievement Journey")
achievements = [
    "Completed 100+ successful web development projects",
    "Mastered HTML, CSS, TypeScript, Python, and currently learning Next.js",
    "Designed and launched multiple responsive web applications",
    "Improved user experience, increasing engagement by 30%"
]

# Display achievements in a more engaging way
for i, achievement in enumerate(achievements, 1):
    st.markdown(f"""
        <div style='
            background-color: #ffffff;
            padding: 15px;
            border-radius: 8px;
            margin: 10px 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            border-left: 4px solid #2E4057;
        '>
        🎯 {achievement}
        </div>
    """, unsafe_allow_html=True)

# Summary section at the bottom
st.markdown("### 📊 Today's Summary")
if user_challenge or reflection:
    st.markdown("""
        <div style='
            background-color: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
        '>
    """, unsafe_allow_html=True)
    
    if user_challenge:
        st.markdown(f"**Today's Challenge:** {user_challenge}")
    
    if reflection:
        st.markdown(f"**Your Reflection:** {reflection}")
    
    # Add timestamp
    st.markdown(f"*Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")
    
    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
    <div style='
        text-align: center;
        padding: 20px;
        color: #666;
        margin-top: 50px;
    '>
        Keep growing, keep learning! 🌱
    </div>
""", unsafe_allow_html=True)
