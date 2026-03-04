import requests
import re
import random
import os
def generate_script():
    # Pick random tool


    base_dir = os.path.dirname(os.path.abspath(__file__))
    tools_path = os.path.join(base_dir, "tools.txt")

    with open(tools_path, "r", encoding="utf-8") as f:
        tools = [line.strip() for line in f if line.strip()]

    topic = random.choice(tools)

    prompt = f"""
    You are a professional YouTube Shorts scriptwriter.

    Generate a high-energy, clean voiceover script for a YouTube Shorts video.

    Topic: AI Tool Spotlight - {topic}

    STRICT RULES:
    - This is a voiceover script only.
    - Do NOT include timestamps.
    - Do NOT include Host:, Narrator:, Scene:, Background:, Music:, or any stage directions.
    - Do NOT include brackets like [ ] or ( ).
    - Do NOT describe visuals.
    - Do NOT include camera instructions.
    - Do NOT include formatting sections inside the script.
    - The SCRIPT must contain ONLY spoken narration text.
    - Write in short, punchy sentences.
    - Make it sound modern and exciting.
    - Optimized for TikTok / Reels style delivery.

    Content Requirements:
    - 60–90 seconds length
    - Start with a strong hook in the first sentence
    - Clearly explain what the tool does
    - Mention who it helps
    - Include 2–3 practical real-world use cases
    - End with a strong call-to-action

    Return EXACTLY in this format:

    TITLE:
    <short viral title>

    SCRIPT:
    <voiceover narration only, plain paragraph text>

    DESCRIPTION:
    <SEO friendly description with hashtags>
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