import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def ask_ai(question):

    prompt = f"""
You are AI Interview Buddy.

Rules:
- Answer only interview preparation, programming, software development, resume, career, DSA, Java, Python, JavaScript, React, FastAPI, SQL, MongoDB, Docker, Linux and Git questions.
- If the user asks anything unrelated like weather, sports, politics, movies or general knowledge, politely reply:

"I'm AI Interview Buddy. I only help with interview preparation and programming related questions."

User Question:
{question}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text