🚀 AI YouTube Automation Engine

An end-to-end AI-powered YouTube content automation system that:

    🧠 Generates scripts using LLaMA (Ollama API)
    
    🎙 Converts script to voice using TTS
    
    🎬 Creates vertical subtitle videos with MoviePy
    
    🎵 Adds random background music (auto-safe handling)
    
    📤 Automatically uploads to YouTube using n8n
    
    🔄 Fully production-ready workflow

📌 Features

    ✅ Random AI tool topic generator
    
    ✅ Structured script generation (Title, Script, Description)
    
    ✅ Automatic subtitle rendering
    
    ✅ Background music with low volume mixing
    
    ✅ Skips broken audio files automatically
    
    ✅ Fully automated YouTube upload
    
    ✅ Production mode (no manual clicks)

🏗 Architecture
            LLaMA (Ollama API)
                    ↓
            Script Generator
                    ↓
            TTS (pyttsx3)
                    ↓
            MoviePy Video Generator
                    ↓
            Random Background Music Mixer
                    ↓
            n8n Webhook
                    ↓
            YouTube Upload API
📂 Project Structure
        youtube_automation/
        │
        ├── main.py
        ├── script_generator.py
        ├── tts_generator.py
        ├── video_generator.py
        ├── tools.txt
        │
        ├── assets/
        │   ├── backgrounds/
        │   └── music/
        │
        ├── output/
        └── README.md
🛠 Requirements

    Install dependencies:
    
    pip install moviepy pyttsx3 pillow numpy requests
    
    Also required:
    
    Ollama running locally
    
    LLaMA model installed
    
    n8n installed and running
    
    YouTube Data API configured in Google Cloud

⚙️ Setup Guide (Step-by-Step)
    🔹 Step 1 — Setup Ollama
    
    Install Ollama and run:
    
    ollama pull llama3
    ollama run llama3
    
    Make sure this endpoint works:
    
    http://localhost:11434/api/generate
<img width="1917" height="968" alt="Screenshot 2026-03-04 053631" src="https://github.com/user-attachments/assets/20988cc0-f7c5-4022-b962-f6c28083030d" />
  🔹 Step 2 — Configure n8n

    Install and run n8n:
    
    n8n
    
    Create a Webhook node:
    
    Method: POST
    
    Path: youtube-upload
    
    Add YouTube Upload node:
    
    Binary Field: data0
    
    Title: {{$json["title"]}}
    
    Description: {{$json["description"]}}
    
    Connect Webhook → YouTube node.
    
    Click Publish.

🔹 Step 3 — Setup Google Cloud

    Create project
    
    Enable YouTube Data API v3
    
    Configure OAuth Consent Screen
    
    Create OAuth 2.0 Client (Web Application)
    
    Add redirect URI from n8n
    
    Connect OAuth inside n8n YouTube node

🔹 Step 4 — Add Background Assets

      Place:
      
      Vertical images in:
      
      assets/backgrounds/
      
      Royalty-free instrumental music in:
      
      assets/music/
      
      ⚠️ Use Content-ID safe music only.

🔹 Step 5 — Run Production Mode

    In main.py, ensure webhook URL is:
    
    http://localhost:5678/webhook/youtube-upload
    
    Then simply run:
    
    python main.py
    
    That’s it.
    
    No manual steps required.

🎬 What Happens When You Run

    Random topic selected
    
    AI generates script
    
    Script converted to speech
    
    Subtitles rendered
    
    Random background music added (low volume)
    
    Video rendered vertically (Shorts format)
    
    Auto-uploaded to YouTube
    
    Title & description dynamically applied

🧠 Stability Features

    Retries script generation if parsing fails
  
    Skips broken MP3 files automatically
    
    Prevents empty script crashes

    Cleans resources to avoid Windows file locks

🔒 Notes on Copyright

    If YouTube blocks video due to music:
    
    Use YouTube Audio Library
    
    Use royalty-free content-ID safe tracks
    
    Or generate your own instrumental loops

📈 Future Improvements

    Auto thumbnail generation
    
    Scheduled publishing
    
    Auto hashtag optimization
    
    AI-generated background music
    
    Cloud deployment
    
    Analytics dashboard

👨‍💻 Author

    Yogesh Kanna
    B.Tech Artificial Intelligence
    AI & Automation Enthusiast
    
    GitHub: https://github.com/YogeshKanna1206

⭐ Why This Project Matters

    This project demonstrates:
    
    AI system design
    
    Full-stack automation
    
    API integrations
    
    LLM pipeline handling
    
    Video processing
    
    Production-level error handling
    
    Dev workflow with Git branches

🚀 Final Result

    Fully automated AI YouTube content engine.
    
    One command:
    
    python main.py
    
    Video generated → Uploaded → Done.
