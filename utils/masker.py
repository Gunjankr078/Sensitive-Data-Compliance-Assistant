import re


def mask_value(category, value):
    """Mask sensitive values before displaying them."""

    # Email
    if "Email" in category:
        parts = value.split("@")
        if len(parts) == 2:
            username = parts[0]
            if len(username) > 4:
                return username[:4] + "*" * (len(username) - 4) + "@" + parts[1]
        return value

    # Phone
    elif "Phone" in category:
        if len(value) >= 10:
            return value[:2] + "*" * 6 + value[-2:]
        return value

    # Aadhaar
    elif "Aadhaar" in category:
        return "********" + value[-4:]

    # PAN
    elif "PAN" in category:
        return value[:2] + "******" + value[-2:]

    # Credit Card
    elif "Credit" in category:
        return "************" + value[-4:]

    # Bank Account
    elif "Bank" in category:
        return "*" * (len(value) - 4) + value[-4:]

    return value    