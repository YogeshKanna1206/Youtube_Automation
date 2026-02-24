import requests
import re
from tts_generator import text_to_speech

def generate_script(topic: str):
    prompt = f"""
    Generate a YouTube video script.

    Topic: {topic}

    Requirements:
    - Duration: 2 minutes
    - Engaging intro
    - Clear explanation
    - Simple language
    - Strong call-to-action at the end

    Format EXACTLY like this:

    TITLE:
    <title here>

    SCRIPT:
    <script here>

    DESCRIPTION:
    <description here>
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    text = response.json()["response"]

    # Extract sections
    title = re.search(r"TITLE:\s*(.*)", text)
    script = re.search(r"SCRIPT:\s*(.*?)DESCRIPTION:", text, re.DOTALL)
    description = re.search(r"DESCRIPTION:\s*(.*)", text, re.DOTALL)

    return {
        "title": title.group(1).strip() if title else "",
        "script": script.group(1).strip() if script else "",
        "description": description.group(1).strip() if description else ""
    }

