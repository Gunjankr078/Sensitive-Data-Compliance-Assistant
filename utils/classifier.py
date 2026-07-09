def classify_risk(detected):

    total = sum(len(v) for v in detected.values())

    if total <= 2:
        return "🟢 Low Risk"

    elif total <= 6:
        return "🟡 Medium Risk"

    else:
        return "🔴 High Risk"