from google.genai import types
from google import genai
client = genai.Client(api_key="AIzaSyCSCRftxtY4Ue51JNusX7XoyO-uzvFxRWc")

prompt = """
You are an expert in insurance policy analysis. Given an insurance-related document, your task is to:

1. Extract all essential details, including:
   - Type of insurance policy  
   - Coverage scope and limits  
   - Premium amount and frequency  
   - Terms and duration  
   - Claim process and requirements  
   - Exclusions and limitations  
   - Obligations of the policyholder and insurer  

2. Identify key points and benefits of the policy.

3. Detect and list any potential loopholes, vague wording, or hidden conditions that may:
   - Affect claim eligibility  
   - Reduce coverage unexpectedly  
   - Introduce legal ambiguity  
4. Say only about the necessary details about the documents when the user is asked as prompt
   prompt : {user_prompt}

Return your output in a structured format with clear section headers:
- Key Details  
- Benefits & Highlights  
- Potential Loopholes & Ambiguities  
- Make the output in neatly order with heading and subpoints
"""

with open('doc.pdf', 'rb') as f:
  image_bytes = f.read()
  response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=[
      types.Part.from_bytes(
        data=image_bytes,
        mime_type='application/pdf',
      ),
      prompt
    ]
  )


print(response.text)