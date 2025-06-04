import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from llm.llm_chain import llm_triage_decision
from rules.triage_rules import rule_based_triage
from utils.explain import generate_explanation




# streamlit_app/app.py

import streamlit as st
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from llm.llm_chain import llm_triage_decision
from rules.triage_rules import rule_based_triage
from utils.explain import generate_explanation

st.set_page_config(page_title="Healthcare Triage Chatbot", page_icon="🩺")

st.title("🩺 AI-Powered Healthcare Chatbot")
st.markdown("Select or describe your symptoms below. The system will suggest what level of care you may need.")

# --- Symptom Options ---
common_symptoms = [
    "Chest pain", "Shortness of breath", "Fever", "Cough", "Vomiting",
    "Dizziness", "Mild headache", "Runny nose", "Sore throat", "Infection",
    "Fatigue", "Rash", "Loss of consciousness", "Severe bleeding"
]

# Multiselect dropdown
selected = st.multiselect("Select symptoms you're experiencing:", common_symptoms)

# Free-text input
typed = st.text_area("Or describe additional symptoms:")

# Combine both
user_input = ", ".join(selected) + ". " + typed.strip()

# Optional: Help section
with st.expander("❓ Need help? See common symptoms"):
    st.write(", ".join(common_symptoms))

# Submit button
if st.button("Analyze"):
    if not user_input.strip():
        st.warning("Please select or describe your symptoms.")
    else:
        with st.spinner("Analyzing your symptoms..."):
            rule_decision = rule_based_triage(user_input)
            llm_decision = llm_triage_decision(user_input)

            # Combine logic
            final_decision = rule_decision if rule_decision == "Seek emergency help now" else llm_decision
            explanation = generate_explanation(user_input, final_decision)

        # Emergency section
        if final_decision == "Seek emergency help now":
            st.error("🚨 Immediate Attention Required!")
            st.markdown("### 🩹 Emergency First Aid Suggestions:")

            if "chest pain" in user_input.lower():
                st.markdown("- **Sit upright** and stay calm.")
                st.markdown("- **Avoid physical activity**.")
                st.markdown("- **Chew aspirin** (if not allergic).")

            if "bleeding" in user_input.lower():
                st.markdown("- **Apply pressure** to the wound.")
                st.markdown("- **Use clean cloth** to control bleeding.")

            if "breath" in user_input.lower() or "breathing" in user_input.lower():
                st.markdown("- **Loosen tight clothing**.")
                st.markdown("- **Open windows** or get fresh air.")
                st.markdown("- **Sit upright**, don’t lie down.")

            st.markdown("- 🚑 **Call emergency services immediately**.")

        # Normal or hospital-level suggestion
        st.success(f"### Suggested Action: **{final_decision}**")
        st.markdown(f"**Reasoning:** {explanation}")
