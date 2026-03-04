import requests

video_path = r"C:\Users\yoges\.n8n-files\videos\final_video.mp4"

with open(video_path, "rb") as f:
    response = requests.post(
        "http://localhost:5678/webhook-test/youtube-upload",
        files={
            "data": ("final_video.mp4", f, "video/mp4")
        }
    )

print(response.status_code)