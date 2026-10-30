
import os, datetime
from topic_engine import get_topic
from script_engine import write_script
from voice_engine import create_voiceover
from video_engine import create_video
from thumbnail_engine import create_thumbnail
from email_engine import send_notification

os.makedirs("output", exist_ok=True)
print("VAYNZOX FREE Starting...")

topic = get_topic()
print(f"Topic: {topic['title']}")

script = write_script(topic)
with open(f"output/{datetime.date.today()}_SCRIPT.txt","w",encoding="utf-8") as f: f.write(script)

audio = create_voiceover(script)
video = create_video(audio, topic)
thumb = create_thumbnail(topic)

with open(f"output/{datetime.date.today()}_META.txt","w",encoding="utf-8") as f:
    f.write(f"TITLE: {topic['title']}\nDESC: {topic['description']}\nKEYWORDS: {', '.join(topic.get('keywords',[]))}\nTHUMB: {topic.get('thumbnail_text','')}")

send_notification(topic, video, thumb)
print("DONE FREE VERSION")
