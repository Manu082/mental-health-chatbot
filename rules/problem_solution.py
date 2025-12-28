def detect_problems(processed_text):
    """
    Detect health-related problems from lemmatized text
    """
    problems = []

    keyword_map = {
        "headache": ["headache", "migraine", "head pain"],
        "fever": ["fever", "temperature"],
        "cold": ["cold", "sneeze", "runny nose"],
        "cough": ["cough", "throat"],
        "stomach": ["stomach", "acidity", "gas", "indigestion"],
        "body_pain": ["body pain", "muscle pain", "back pain"],
        "vomiting": ["vomit", "vomiting", "nausea"],
        "blood_pressure": ["blood pressure", "bp", "high bp", "low bp"],
        "anxiety": ["anxiety", "anxious", "stress", "panic"],
        "depression": ["depress", "sad", "hopeless"],
        "insomnia": ["insomnia", "sleep problem", "not sleeping"],
        "weakness": ["weak", "fatigue", "tired"]
    }

    for problem, words in keyword_map.items():
        for w in words:
            if w in processed_text:
                problems.append(problem)
                break

    return problems


def get_care_solutions(problem):
    """
    Return non-medical care and lifestyle solutions
    """
    care_map = {
        "headache": [
            "Rest in a quiet and dark place",
            "Drink plenty of water",
            "Avoid long screen exposure"
        ],

        "fever": [
            "Take adequate rest",
            "Drink fluids frequently",
            "Monitor body temperature"
        ],

        "cold": [
            "Steam inhalation",
            "Drink warm fluids",
            "Avoid cold environments"
        ],

        "cough": [
            "Warm water gargle",
            "Avoid cold drinks",
            "Rest your throat"
        ],

        "stomach": [
            "Eat light and easily digestible food",
            "Avoid spicy and oily food",
            "Stay hydrated"
        ],

        "body_pain": [
            "Use warm compress",
            "Do gentle stretching",
            "Avoid heavy physical activity"
        ],

        "vomiting": [
            "Take small sips of water or ORS",
            "Avoid oily and spicy food",
            "Rest and avoid sudden movements"
        ],

        "blood_pressure": [
            "Reduce salt intake",
            "Practice deep breathing and relaxation",
            "Monitor blood pressure regularly"
        ],

        "anxiety": [
            "Practice deep breathing exercises",
            "Take a short walk or light exercise",
            "Reduce caffeine intake"
        ],

        "depression": [
            "Talk to someone you trust",
            "Maintain a daily routine",
            "Engage in light physical activity"
        ],

        "insomnia": [
            "Maintain a fixed sleep schedule",
            "Avoid screen time before bed",
            "Practice relaxation before sleep"
        ],

        "weakness": [
            "Eat nutritious food",
            "Get adequate sleep",
            "Stay hydrated"
        ]
    }

    return care_map.get(problem, ["Take proper rest and consult a healthcare professional"])


def get_tablet_suggestions(problem):
    """
    Return tablet suggestions (awareness only, not prescription)
    """
    tablet_map = {
        "headache": "Paracetamol",
        "fever": "Paracetamol",
        "cold": "Cetirizine",
        "cough": "Cough Syrup (Benadryl type)",
        "stomach": "Antacid (ENO / Gelusil)",
        "body_pain": "Paracetamol",
        "vomiting": "ORS / Ondansetron (doctor advised)",
        "blood_pressure": "⚠️ BP medicines require doctor prescription",
        "insomnia": "Melatonin (low dose)",
        "weakness": "Multivitamin",
        "anxiety": "⚠️ No self-medication recommended",
        "depression": "⚠️ Doctor consultation required"
    }

    return tablet_map.get(problem, "Consult a doctor")
