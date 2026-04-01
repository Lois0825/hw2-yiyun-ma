import google.generativeai as genai
import os


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def generate_email(notes):
    prompt = f"""
Write a professional follow-up email based on these meeting notes:

{notes}
"""

    response = model.generate_content(prompt)
    return response.text


if __name__ == "__main__":
    notes = input("Enter meeting notes: ")
    result = generate_email(notes)
    
    print("\nGenerated Email:\n")
    print(result)
