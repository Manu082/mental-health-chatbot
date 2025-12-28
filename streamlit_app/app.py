import streamlit as st
import sys
import os

# Path setup
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.nlp.preprocess import preprocess_text
from rules.emotion_rules import detect_emotion, get_response
from rules.problem_solution import (
    detect_problems,
    get_care_solutions,
    get_tablet_suggestions
)

# Page config
st.set_page_config(
    page_title="Mental Health Chatbot",
    page_icon="🧠",
    layout="centered"
)

# Sidebar
st.sidebar.title("⚙️ Settings")
st.sidebar.write("Emotion-aware NLP Chatbot")
if st.sidebar.button("🗑 Clear Chat"):
    st.session_state.chat_history = []

# Main UI
st.title("🧠 Mental Health Support Chatbot")
st.caption("An interactive NLP-based chatbot using Lemmatization")

# Session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for speaker, msg, emo in st.session_state.chat_history:
    if speaker == "You":
        st.markdown(f"🧍 **You:** {msg}")
    else:
        st.markdown(f"🤖 **Bot ({emo.upper()}):** {msg}")

# Input section
st.divider()
user_input = st.text_input("💬 How are you feeling today?")

if st.button("Send 💌"):
    if user_input.strip():
        # NLP preprocessing
        processed = preprocess_text(user_input)

        # Emotion detection
        emotion = detect_emotion(processed)
        response = get_response(emotion)

        # Problem detection
        problems = detect_problems(processed)

        # Store conversation
        st.session_state.chat_history.append(("You", user_input, ""))
        st.session_state.chat_history.append(("Bot", response, emotion))

        # Emotion result
        st.success(f"Detected Emotion: **{emotion.upper()}**")

        # Care & solution section
        if problems:
            st.subheader("🩺 Suggested Care & Solutions")
            for problem in problems:
                st.markdown(f"**🔹 {problem.capitalize()}**")
                care_steps = get_care_solutions(problem)
                for step in care_steps:
                    st.markdown(f"- {step}")

            # Tablet section (NEW, separate & below)
            st.subheader("💊 Tablet Suggestions (Awareness Only)")
            for problem in problems:
                tablet = get_tablet_suggestions(problem)
                st.markdown(f"**{problem.capitalize()}:** {tablet}")

            st.warning(
                "⚠️ Tablet suggestions are for educational awareness only. "
                "Please consult a doctor before taking any medication."
            )
