from google.genai import types
from google import genai


def analyze_prompt_with_document(prompt, pdf_path) -> str:
    client = genai.Client(api_key="YOUR_GEMENI_API_KEY")

    insurance_prompt = """

You are a top-tier legal policy analyst with expertise in uncovering hidden clauses, vague terms, and document loopholes. Analyze the terms in:

Apply this framework: identify ambiguous exclusions, privacy risks, hidden fees, or dispute limitations.

Cross-verify claims in these pages. Prioritize:

1. High-impact loopholes
2. Obscure legal phrasing
3. Inconsistencies between privacy and terms of usage

Output:
- In plain English
- ≤ 50 words
- Flag the most critical risks clearly

Act as a consumer protection watchdog. Use clear, bold warnings if needed.

"""
    if prompt != "SUMMARY":
        prompt = prompt + ", do not use(*, #) instead use (1,2 for numbered output and also please use <br> tag from the starting when numbered output is used)  in the output please give the output in a neatway."
    else:
        prompt = insurance_prompt
    with open(pdf_path, "rb") as f:
        image_bytes = f.read()
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                types.Part.from_bytes(
                    data=image_bytes,
                    mime_type="application/pdf",
                ),
                prompt,
            ],
        )
    return response.text

"""4. Say only about the necessary details about the documents when the user is asked as prompt
   prompt : ```{prompt}```
"""