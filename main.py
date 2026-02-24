from script_generator import generate_script
import os
from tts_generator import text_to_speech
from video_generator import generate_video


def save_output(data):
    os.makedirs("output", exist_ok=True)

    with open("output/title.txt", "w", encoding="utf-8") as f:
        f.write(data["title"])

    with open("output/script.txt", "w", encoding="utf-8") as f:
        f.write(data["script"])

    with open("output/description.txt", "w", encoding="utf-8") as f:
        f.write(data["description"])


def run():
    topic = "Binary Search explained for coding interviews"

    print("🧠 Generating script...")
    content = generate_script(topic)

    save_output(content)
    print("✅ Title, Script, and Description saved separately.")

    # 🔥 Now convert script to audio
    print("🎙 Generating audio...")
    text_to_speech(content["script"], "output/audio.mp3")
    print("✅ Audio saved at output/audio.mp3")
    print("🎬 Generating video...")
    generate_video("output/audio.mp3", content["script"], "output/final_video.mp4")
    print("✅ Video saved at output/final_video.mp4")

if __name__ == "__main__":
    run()