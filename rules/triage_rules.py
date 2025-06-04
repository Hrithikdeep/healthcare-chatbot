# rules/triage_rules.py

def rule_based_triage(symptoms: str) -> str:
    """
    Basic rule-based triage system.
    Returns one of:
    - "Stay home and monitor"
    - "Visit hospital soon"
    - "Seek emergency help now"
    """
    symptoms = symptoms.lower()

    emergency_keywords = ["chest pain", "shortness of breath", "severe bleeding", "loss of consciousness"]
    hospital_keywords = ["fever", "cough", "vomiting", "dizziness", "rash", "infection"]
    stay_home_keywords = ["mild headache", "runny nose", "tiredness", "sore throat"]

    if any(word in symptoms for word in emergency_keywords):
        return "Seek emergency help now"
    elif any(word in symptoms for word in hospital_keywords):
        return "Visit hospital soon"
    elif any(word in symptoms for word in stay_home_keywords):
        return "Stay home and monitor"
    else:
        return "Visit hospital soon"  # Default to safe option
