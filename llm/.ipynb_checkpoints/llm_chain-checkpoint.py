from langchain.llms import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from transformers import pipeline

def get_llm_chain():
    pipe = pipeline("text-generation", model="microsoft/BioGPT", max_length=100)
    llm = HuggingFacePipeline(pipeline=pipe)

    prompt = PromptTemplate(
        input_variables=["symptoms"],
        template="Patient reports: {symptoms}\nWhat should be the action? Respond only with: Stay home and monitor / Visit hospital soon / Seek emergency help now"
    )

    chain = LLMChain(prompt=prompt, llm=llm)
    return chain

def llm_triage(symptoms):
    chain = get_llm_chain()
    result = chain.run({"symptoms": symptoms})
    return result.strip()
