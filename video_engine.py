
from moviepy.editor import *
import os

def create_video(audio_path, topic_data):
    try:
        if audio_path.endswith(".mp3") and os.path.exists(audio_path):
            audio = AudioFileClip(audio_path)
            duration = audio.duration
        else:
            duration = 60
            audio = None

        # Simple pro video - black bg + title
        txt = TextClip(topic_data['title'], fontsize=65, color='white', size=(1920,1080), method='caption', font='Arial-Bold').set_duration(duration).set_position('center')
        bg = ColorClip(size=(1920,1080), color=(12,12,12)).set_duration(duration)
        final = CompositeVideoClip([bg, txt])
        if audio:
            final = final.set_audio(audio)

        out = f"output/VIDEO_{topic_data['title'][:20].replace(' ','_')}.mp4"
        final.write_videofile(out, fps=24, codec='libx264', audio_codec='aac')
        return out
    except Exception as e:
        print(f"Video error {e}")
        return audio_path
