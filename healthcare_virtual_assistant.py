
import streamlit as st

st.set_page_config(page_title="Healthcare Virtual Assistant", layout="centered")

st.title("🩺 Healthcare AI Virtual Assistant")
st.write("Hi! I'm your friendly healthcare assistant. How can I help you today?")

user_input = st.text_input("Ask a question...")

def get_response(user_input):
    responses = {
        "appointment": "Sure! Please provide your preferred date and time.",
        "schedule": "I can help schedule an appointment. When would you like to come in?",
        "fever": "I'm not a doctor, but it sounds like a common symptom. Please rest, stay hydrated, and consult a physician if it persists.",
        "covid": "If you're experiencing COVID-19 symptoms, please isolate and contact your healthcare provider for further instructions.",
        "faq": "Here are some common FAQs:\n- Opening hours: 9AM–5PM\n- Contact: 123-456-7890\n- Address: 123 Health St."
    }
    for keyword in responses:
        if keyword in user_input.lower():
            return responses[keyword]
    return "I'm here to help with scheduling, FAQs, or basic symptom info. Please rephrase your question."

if user_input:
    response = get_response(user_input)
    st.write(f"💬 {response}")
