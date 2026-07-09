import re
from utils.patterns import PATTERNS


def detect_sensitive_data(text):

    # If extraction failed or there's nothing to scan, return no detections.
    if not text or not str(text).strip():
        return {}

    detected = {}

    for name, pattern in PATTERNS.items():

        matches = re.findall(pattern, text)

        if matches:
            detected[name] = matches

    return detected
