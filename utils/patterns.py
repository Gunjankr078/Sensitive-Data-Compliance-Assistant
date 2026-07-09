import re

PATTERNS = {

    "Aadhaar Number": r"\b\d{4}\s?\d{4}\s?\d{4}\b",

    "PAN Number": r"\b[A-Z]{5}[0-9]{4}[A-Z]{1}\b",

    "Email Address": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",

    "Phone Number": r"\b(?:\+91[-\s]?)?[6-9]\d{9}\b",

    "Credit Card": r"\b(?:\d{4}[- ]?){3}\d{4}\b",

    "Bank Account": r"\b\d{9,18}\b",

    "IFSC Code": r"\b[A-Z]{4}0[A-Z0-9]{6}\b",

    "API Key": r"\b(?:sk|AIza)[A-Za-z0-9\-_]{20,}\b",

    "Password": r"(?i)(password|passwd|pwd)\s*[:=]\s*\S+",

    "Employee ID": r"\bEMP\d{3,6}\b"

}