import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")  # Placeholder for real API key

MODEL = "gpt-3.5-turbo"

def query_openai(prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response['choices'][0]['message']['content'].strip()