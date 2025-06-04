
# utils/explain.py

def generate_explanation(symptoms: str, decision: str) -> str:
    """
    Provide a simple explanation for the triage decision.
    """

    symptoms = symptoms.lower()

    if decision == "Seek emergency help now":
        if "chest pain" in symptoms or "shortness of breath" in symptoms:
            return "You need emergency care due to symptoms like chest pain or shortness of breath."
        else:
            return "You reported severe symptoms that require emergency attention."

    elif decision == "Visit hospital soon":
        return "You may need to see a doctor soon based on symptoms like fever, infection, or other moderate issues."

    elif decision == "Stay home and monitor":
        return "Your symptoms seem mild (e.g., tiredness or runny nose), so home care may be sufficient for now."

    else:
        return "Unable to generate explanation."
