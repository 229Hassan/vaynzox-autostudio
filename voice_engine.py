
import asyncio, edge_tts, os

async def _make_voice(text, path):
    # Guy - American news anchor voice, best for geopolitics - FREE
    voice = "en-US-GuyNeural" 
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(path)

def create_voiceover(script_text):
    # edge-tts needs max 5000 chars per call, so we trim for free version
    text = script_text[:5000]
    path = "output/voiceover.mp3"
    try:
        asyncio.run(_make_voice(text, path))
        return path
    except Exception as e:
        print(f"Voice error {e}")
        with open("output/voiceover.txt","w",encoding="utf-8") as f: f.write(text)
        return "output/voiceover.txt"
