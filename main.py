from script_generator import generate_script
import os
from tts_generator import text_to_speech
from video_generator import generate_video
import requests
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
    content = generate_script()

    save_output(content)
    print("✅ Title, Script, and Description saved separately.")

    # 🔥 Now convert script to audio
    print("🎙 Generating audio...")
    text_to_speech(content["script"], "output/audio.mp3")
    print("✅ Audio saved at output/audio.mp3")
    print("🎬 Generating video...")
    output_dir = r"C:\Users\yoges\.n8n-files\videos"
    os.makedirs(output_dir, exist_ok=True)

    video_path = os.path.join(output_dir, "final_video.mp4")
    generate_video("output/audio.mp3", content["script"], video_path)
    print("✅ Video saved at output/final_video.mp4")

    video_path = r"C:\Users\yoges\.n8n-files\videos\final_video.mp4"

    title = content["title"]
    description = content["description"]

    with open(video_path, "rb") as f:
        response = requests.post(
            "http://localhost:5678/webhook/youtube-upload",
            files={
                "data": ("final_video.mp4", f, "video/mp4")
            },
            data={
                "title": title,
                "description": description
            }
        )

    print(response.status_code)

if __name__ == "__main__":
    run()