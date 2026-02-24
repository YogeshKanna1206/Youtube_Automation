import os
from PIL import Image, ImageDraw, ImageFont
import numpy as np

from moviepy.video.VideoClip import ImageClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip


def create_text_image(text, width=900, height=300):
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", 60)
    except:
        font = ImageFont.load_default()

    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    x = (width - text_width) / 2
    y = (height - text_height) / 2

    draw.text((x, y), text, font=font, fill="white")

    return np.array(img)


def generate_video(audio_path, script_text, output_path):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(base_dir, "assets", "background.png")

    audio = AudioFileClip(audio_path)

    background = (
        ImageClip(image_path)
        .resized(height=1920)
        .cropped(x_center=540, width=1080)
        .with_duration(audio.duration)
        .resized(lambda t: 1 + 0.02 * t)
    )

    lines = script_text.split(". ")
    duration_per_line = audio.duration / max(len(lines), 1)

    subtitle_clips = []

    for i, line in enumerate(lines):
        img_array = create_text_image(line.strip())
        txt_clip = (
            ImageClip(img_array)
            .with_duration(duration_per_line)
            .with_start(i * duration_per_line)
            .with_position(("center", 1400))
        )

        subtitle_clips.append(txt_clip)

    final_video = CompositeVideoClip(
        [background] + subtitle_clips
    ).with_audio(audio)

    final_video.write_videofile(output_path, fps=30)