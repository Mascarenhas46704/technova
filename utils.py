import json

def load_adr_rules(path="adr_rules.json"):
    """
    Loads ADR rules from a JSON file.
    Returns a dictionary mapping symptoms to a list of suspect medications.
    """
    with open(path, "r") as file:
        return json.load(file)

def detect_adr(symptoms, medications, adr_rules):
    """
    Detects possible ADRs based on provided symptoms and medications.
    
    Parameters:
      symptoms (list): List of symptoms provided (lowercase strings)
      medications (list): List of medications provided (lowercase strings)
      adr_rules (dict): ADR rule mapping
      
    Returns:
      alerts (list): List of dicts containing alert details.
    """
    alerts = []
    for symptom in symptoms:
        if symptom in adr_rules:
            for med in medications:
                rule_meds = [m.lower() for m in adr_rules[symptom]]
                if med in rule_meds:
                    alerts.append({
                        "symptom": symptom,
                        "medication": med,
                        "severity": "⚠️ High"
                    })
    return alerts
