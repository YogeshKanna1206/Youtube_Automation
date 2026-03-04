import os
import random
import textwrap
import numpy as np
from PIL import Image, ImageDraw, ImageFont

from moviepy.video.VideoClip import ImageClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.audio.AudioClip import CompositeAudioClip


# -----------------------------
# TEXT IMAGE CREATION
# -----------------------------
def create_text_image(text, width=720, height=1280):
    img = Image.new("RGBA", (width, height), (0, 0, 0, 180))
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", 55)
    except:
        font = ImageFont.load_default()

    wrapped_text = textwrap.fill(text, width=20)

    text_bbox = draw.multiline_textbbox((0, 0), wrapped_text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    x = (width - text_width) / 2
    y = (height - text_height) / 2

    draw.multiline_text(
        (x, y),
        wrapped_text,
        font=font,
        fill="white",
        align="center"
    )

    return np.array(img)


# -----------------------------
# MAIN VIDEO GENERATION
# -----------------------------
def generate_video(audio_path, script_text, output_path):
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Load voice
    voice_audio = AudioFileClip(audio_path)

    # -----------------------------
    # RANDOM BACKGROUND IMAGE
    # -----------------------------
    bg_folder = os.path.join(base_dir, "assets", "backgrounds")
    images = [img for img in os.listdir(bg_folder)
              if img.endswith((".png", ".jpg", ".jpeg"))]

    random_bg = random.choice(images)
    image_path = os.path.join(bg_folder, random_bg)

    print("🖼 Using background:", random_bg)

    background = (
        ImageClip(image_path)
        .resized(height=1280)
        .cropped(x_center=360, width=720)
        .with_duration(voice_audio.duration)
    )

    # -----------------------------
    # SAFE RANDOM MUSIC LOADER
    # -----------------------------
    music_folder = os.path.join(base_dir, "assets", "music")
    music_files = [m for m in os.listdir(music_folder)
                   if m.endswith(".mp3")]

    random.shuffle(music_files)

    bg_music = None

    for music_file in music_files:
        try:
            music_path = os.path.join(music_folder, music_file)
            print("🎵 Trying music:", music_file)

            bg_music = AudioFileClip(music_path)
            print("✅ Using music:", music_file)
            break

        except Exception:
            print("❌ Skipping broken file:", music_file)

    # -----------------------------
    # AUDIO MIXING
    # -----------------------------
    if bg_music:
        if bg_music.duration < voice_audio.duration:
            bg_music = bg_music.looped(duration=voice_audio.duration)

        bg_music = bg_music.subclipped(0, voice_audio.duration)
        bg_music = bg_music.with_volume_scaled(0.15)

        final_audio = CompositeAudioClip([bg_music, voice_audio])
    else:
        print("⚠ No valid music found. Using voice only.")
        final_audio = voice_audio

    # -----------------------------
    # SUBTITLES
    # -----------------------------
    lines = script_text.split(". ")
    duration_per_line = voice_audio.duration / max(len(lines), 1)

    subtitle_clips = []

    for i, line in enumerate(lines):
        img_array = create_text_image(line.strip())

        txt_clip = (
            ImageClip(img_array)
            .with_duration(duration_per_line)
            .with_start(i * duration_per_line)
            .with_position(("center", "center"))
        )

        subtitle_clips.append(txt_clip)

    # -----------------------------
    # FINAL VIDEO
    # -----------------------------
    final_video = CompositeVideoClip(
        [background] + subtitle_clips
    ).with_audio(final_audio)

    final_video.write_videofile(
        output_path,
        fps=20,
        codec="libx264",
        preset="ultrafast"
    )

    # -----------------------------
    # CLEANUP
    # -----------------------------
    final_video.close()
    voice_audio.close()
    if bg_music:
        bg_music.close()