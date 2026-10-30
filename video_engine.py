import os
from moviepy.editor import *
from PIL import Image, ImageDraw, ImageFont

def create_video(audio_path, topic_data):
    try:
        if audio_path.endswith(".mp3") and os.path.exists(audio_path):
            audio = AudioFileClip(audio_path)
            duration = audio.duration
        else:
            duration = 60
            audio = None

        # 1. High quality title image banao (Pillow se - TextClip se tez aur quality best)
        W, H = 1920, 1080
        title_img = Image.new('RGB', (W, H), color=(10, 10, 15))
        draw = ImageDraw.Draw(title_img)
        try:
            font = ImageFont.truetype("DejaVuSans-Bold.ttf", 80)
        except:
            font = ImageFont.load_default()
        
        # Title ko wrap karo
        title = topic_data['title']
        draw.text((100, 400), title, fill=(255, 255, 255), font=font, stroke_width=3, stroke_fill=(0,0,0))
        draw.text((100, 550), "VAYNZOX | Geopolitics x Future Tech", fill=(255, 220, 0), font=font)
        title_img.save("output/title_bg.jpg")

        # 2. Video banao
        bg = ImageClip("output/title_bg.jpg").set_duration(duration)
        if audio:
            bg = bg.set_audio(audio)

        out = f"output/VIDEO_1080p.mp4"
        # High quality settings for TV
        bg.write_videofile(out, fps=30, codec='libx264', audio_codec='aac', bitrate="8000k", audio_bitrate="192k", preset='medium', threads=4)
        return out
    except Exception as e:
        print(f"Video error {e}")
        return audio_path
