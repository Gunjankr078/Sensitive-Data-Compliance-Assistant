def calculate_score(detected_data):
    """
    Calculate compliance score out of 100.
    Higher score = Lower risk.
    """

    score = 100

    penalties = {
        "Email Address": 3,
        "Phone Number": 4,
        "PAN Number": 12,
        "Aadhaar Number": 15,
        "Credit Card": 20,
        "Bank Account": 10,
        "IFSC Code": 5,
        "API Key": 25,
        "Password": 25,
        "Employee ID": 5
    }

    for key, values in detected_data.items():
        score -= penalties.get(key, 2) * len(values)

    return max(score, 0)