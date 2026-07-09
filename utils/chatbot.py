import google.generativeai as genai


def ask_question(api_key, document_text, detected_data, question):

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
        You are an AI Compliance Assistant.

        You must answer ONLY using the uploaded document.

        Rules:
        - Do NOT generate JSON.
        - Do NOT use markdown code blocks.
        - Do NOT wrap the answer inside ``` or {{ }}.
        - Answer in plain English.
        - If the answer is not in the document, say:
          "This information is not available in the uploaded document."

        Uploaded Document:
        {document_text}

        Detected Sensitive Data:
        {detected_data}

        User Question:
        {question}

        Answer:
    """

    try:
        response = model.generate_content(prompt)
        answer = response.text.strip()

        answer = answer.replace("```", "")
        answer = answer.replace("json", "")

        return answer

    except Exception as e:
        return f"⚠️ Unable to answer your question.\n\nReason:\n{str(e)}"