from utils.explain import generate_explanation

def generate_explanation(symptoms, decision):
    if "emergency" in decision.lower():
        return "This may be an emergency due to severe symptoms like chest pain or breathing difficulty."
    elif "hospital" in decision.lower():
        return "Symptoms may need a doctor’s attention, especially if they persist or worsen."
    elif "stay home" in decision.lower():
        return "Symptoms seem mild. Rest, hydrate, and monitor your condition."
    return "Unable to generate explanation."
