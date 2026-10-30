import os
from google import genai

def write_script(topic_data):
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    prompt = f'Write a 1000 word YouTube script for VAYNZOX channel. Title: {topic_data["title"]} Hook: {topic_data["hook"]} Audience: US, 18-45 male. Structure: 1. HOOK (0-20s) - Shocking question 2. CONTEXT (20s-2min) - Geopolitics background 3. DEEP DIVE (2-9min) - Future tech part 4. FUTURE (9-11min) - What happens 2026-2030? 5. CTA (11-12min) - Subscribe. Rules: American English, short sentences, conversational, no Welcome, add [PAUSE] for voice.'
    res = client.models.generate_content(model='gemini-3.8-flash', contents=prompt)
    return res.text
