# Age and Weight-Specific Drug Dosage Calculator

DOSAGE_GUIDELINES = {
    "paracetamol": {  # Example: 15 mg/kg/dose for children, fixed for adults/elderly
        "child": {"mg_per_kg": 15, "max_mg": 1000},
        "adult": {"mg": 500},
        "elderly": {"mg": 400}
    },
    "ibuprofen": {     # Example: 10 mg/kg/dose for children, fixed for adults/elderly
        "child": {"mg_per_kg": 10, "max_mg": 400},
        "adult": {"mg": 400},
        "elderly": {"mg": 300}
    },
    "amoxicillin": {   # Example: 20 mg/kg/dose for children, fixed otherwise
        "child": {"mg_per_kg": 20, "max_mg": 500},
        "adult": {"mg": 500},
        "elderly": {"mg": 500}
    },
    # Remaining drugs have fixed doses for simplicity
    "cetirizine":     {"child": {"mg": 5},   "adult": {"mg": 10},   "elderly": {"mg": 10}},
    "metformin":      {"child": {"mg": 250}, "adult": {"mg": 500},  "elderly": {"mg": 500}},
    "atenolol":       {"child": {"mg": 25},  "adult": {"mg": 50},   "elderly": {"mg": 25}},
    "azithromycin":   {"child": {"mg": 10},  "adult": {"mg": 500},  "elderly": {"mg": 500}},
    "loratadine":     {"child": {"mg": 5},   "adult": {"mg": 10},   "elderly": {"mg": 10}},
    "losartan":       {"child": {"mg": 25},  "adult": {"mg": 50},   "elderly": {"mg": 25}},
    "atorvastatin":   {"child": {"mg": 10},  "adult": {"mg": 20},   "elderly": {"mg": 10}},
    "omeprazole":     {"child": {"mg": 10},  "adult": {"mg": 20},   "elderly": {"mg": 20}},
    "levothyroxine":  {"child": {"mg": 25},  "adult": {"mg": 50},   "elderly": {"mg": 25}},
    "amlodipine":     {"child": {"mg": 2.5}, "adult": {"mg": 5},    "elderly": {"mg": 2.5}},
    "salbutamol":     {"child": {"mg": 2},   "adult": {"mg": 4},    "elderly": {"mg": 2}},
    "diclofenac":     {"child": {"mg": 25},  "adult": {"mg": 50},   "elderly": {"mg": 25}}
}

def get_age_group(age):
    if age < 12:
        return "child"
    elif age >= 65:
        return "elderly"
    else:
        return "adult"

def recommend_dosage(drug, age, weight):
    drug = drug.lower()
    if drug not in DOSAGE_GUIDELINES:
        return None, f"Drug '{drug}' not in database."
    age_group = get_age_group(age)
    guide = DOSAGE_GUIDELINES[drug][age_group]
    # If weight-based dosing applies:
    if "mg_per_kg" in guide:
        dose = weight * guide["mg_per_kg"]
        if "max_mg" in guide:
            dose = min(dose, guide["max_mg"])
        return f"{dose} mg (based on {guide['mg_per_kg']} mg/kg)", None
    elif "mg" in guide:
        return f"{guide['mg']} mg", None
    else:
        return None, "Dosage guideline not available."
    
def main():
    print("Welcome to Age and Weight-Specific Drug Dosage Calculator")
    print("Available drugs:")
    print(', '.join(DOSAGE_GUIDELINES.keys()))
    try:
        age = int(input("Enter patient age (years): "))
        weight = float(input("Enter patient weight (kg): "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return
    drug = input("Enter drug name: ").strip().lower()
    dose, error = recommend_dosage(drug, age, weight)
    if error:
        print(error)
    else:
        print(f"Recommended dosage of {drug.capitalize()} for age {age}, weight {weight} kg: {dose}")

if __name__ == "__main__":
    main()
