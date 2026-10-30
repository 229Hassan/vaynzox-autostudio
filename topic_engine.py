import os
import json
import google.generativeai as genai

def get_topic():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return {"title": "How US Plans to Block China's Internet Cables in 2026", "thumbnail_text": "INTERNET WAR?", "description": "US vs China undersea cable battle.", "keywords": ["geopolitics", "USA", "China"], "hook": "The next world war won't start with nukes, but with a cable cut?"}
    
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = 'You are a viral YouTube strategist for US audience for channel VAYNZOX. Niche: Merge GEOPOLITICS + FUTURE SCIENCE/DIGITAL TECH. Give 1 topic TODAY. US-centric, high CPM. Return ONLY valid JSON: {"title": "...", "thumbnail_text": "2-3 WORDS CAPS", "description": "SEO 2 lines", "keywords": ["...", "..."], "hook": "first line"} Title 45-65 chars. No extra text.'
    try:
        res = model.generate_content(prompt)
        text = res.text.replace('json','').replace('','').strip()
        return json.loads(text)
    except Exception as e:
        print(f"Gemini topic error {e}")
        return {"title": "Why US Undersea Cables Could Trigger WW3 in 2026", "thumbnail_text": "WW3 CABLES?", "description": "US vs China digital war explained.", "keywords": ["geopolitics", "tech"], "hook": "What if cutting one cable could blackout America?"}
