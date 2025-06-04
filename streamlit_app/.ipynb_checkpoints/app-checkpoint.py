import streamlit as st
from rules.triage_rules import rule_based_triage
from llm.llm_chain import llm_triage
from utils.explain import generate_explanation

st.set_page_config(page_title="AI Healthcare Chatbot", layout="centered")

st.title(" AI-Powered Healthcare Chatbot")
st.write("Describe your symptoms below to get a recommendation.")

user_input = st.text_area(" Symptoms", placeholder="e.g., I have high fever and chest pain")

if st.button("Submit"):
    if user_input.strip():
        rule_result = rule_based_triage(user_input)
        llm_result = llm_triage(user_input)

        # Combine logic (LLM is overridden by rule if emergency detected)
        final_result = rule_result if "emergency" in rule_result.lower() else llm_result
        explanation = generate_explanation(user_input, final_result)

        st.subheader(" Recommendation")
        st.success(final_result)

        st.subheader(" Why this recommendation?")
        st.info(explanation)
    else:
        st.warning("Please describe your symptoms first.")
