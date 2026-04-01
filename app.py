import os
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

def generate_email(notes):
    prompt = f"""
Write a professional follow-up email based on these meeting notes:

{notes}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    notes = input("Enter meeting notes: ")
    result = generate_email(notes)
    print("\nGenerated Email:\n")
    print(result)
