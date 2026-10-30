
from PIL import Image, ImageDraw, ImageFont

def create_thumbnail(topic_data):
    W,H = 1280,720
    img = Image.new('RGB', (W,H), color=(10,10,10))
    draw = ImageDraw.Draw(img)
    try:
        font_big = ImageFont.truetype("arial.ttf", 100)
        font_small = ImageFont.truetype("arial.ttf", 50)
    except:
        font_big = ImageFont.load_default()
        font_small = ImageFont.load_default()

    text = topic_data.get('thumbnail_text','BREAKING')
    draw.rectangle([(0,0),(W,120)], fill=(200,0,0))
    draw.text((40,20), "VAYNZOX EXCLUSIVE", fill="white", font=font_small)
    draw.text((50,180), text, fill="white", font=font_big, stroke_width=6, stroke_fill="black")
    draw.text((50,400), "USA vs CHINA", fill=(255,255,0), font=font_big)

    path = f"output/THUMBNAIL.jpg"
    img.save(path)
    return path
