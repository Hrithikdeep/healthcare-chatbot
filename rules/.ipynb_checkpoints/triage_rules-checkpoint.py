def rule_based_triage(symptom_text):
    symptom_text = symptom_text.lower()

    emergency_keywords = ["chest pain", "shortness of breath", "seizure", "stroke", "confusion", "unconscious", "coughing blood", "blue lips"]
    hospital_keywords = ["high fever", "difficulty breathing", "vomiting", "blurred vision", "severe headache", "dizziness", "persistent cough"]
    home_keywords = ["mild fever", "sore throat", "runny nose", "mild headache", "sneezing", "fatigue"]

    for word in emergency_keywords:
        if word in symptom_text:
            return "Seek emergency help now"
    for word in hospital_keywords:
        if word in symptom_text:
            return "Visit hospital soon"
    for word in home_keywords:
        if word in symptom_text:
            return "Stay home and monitor"

    return "Visit hospital soon"
