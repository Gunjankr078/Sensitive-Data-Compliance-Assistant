import google.generativeai as genai


def generate_summary(api_key, text, detected_data):

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
You are a Cyber Security and Compliance Expert.

Analyze the following document.

Document:

{text}

Detected Sensitive Data:

{detected_data}

Return the response in exactly this format.

Observations:
- observation 1
- observation 2

Security Risks:
- risk 1
- risk 2

Recommendations:
- recommendation 1
- recommendation 2
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"⚠️ AI Summary could not be generated.\n\nReason:\n{str(e)}"