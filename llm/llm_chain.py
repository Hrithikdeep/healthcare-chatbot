# llm/llm_chain.py

from langchain_community.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

# Initialize HuggingFace LLM
llm = HuggingFaceHub(
    repo_id="google/flan-t5-large",  # You can try other models later
    model_kwargs={"temperature": 0.5, "max_length": 100}
)

# Define prompt template
triage_prompt = PromptTemplate(
    input_variables=["symptoms"],
    template="Patient reports: {symptoms}. Based on this, what level of care is recommended: Stay home, Visit hospital soon, or Seek emergency help now?"
)

def llm_triage_decision(symptoms: str) -> str:
    """Use LLM to make a triage suggestion based on symptoms."""
    prompt = triage_prompt.format(symptoms=symptoms)
    try:
        response = llm(prompt)
        return response.strip()
    except Exception as e:
        return f"LLM error: {e}"

