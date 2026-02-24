import pyttsx3

def text_to_speech(text: str, filename: str):
    engine = pyttsx3.init()

    # Set voice properties
    engine.setProperty('rate', 150)  # speed
    engine.setProperty('volume', 1)  # volume

    # Save to file
    engine.save_to_file(text, filename)
    engine.runAndWait()