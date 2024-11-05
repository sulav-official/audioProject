import os
from flask import Flask, request, render_template, redirect, url_for
import moviepy.editor as mp
import speech_recognition as sr
from pydub import AudioSegment

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['CHUNK_LENGTH_MS'] = 60000  # Process audio in 1-minute chunks

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def transcribe_audio(audio_path):
    audio = AudioSegment.from_wav(audio_path)
    duration = len(audio)
    recognizer = sr.Recognizer()
    full_text = []

    # Process each chunk of audio
    for i in range(0, duration, app.config['CHUNK_LENGTH_MS']):
        chunk = audio[i:i+app.config['CHUNK_LENGTH_MS']]
        chunk_path = f"chunk_{i//app.config['CHUNK_LENGTH_MS']}.wav"
        chunk.export(chunk_path, format="wav")

        with sr.AudioFile(chunk_path) as source:
            audio_data = recognizer.record(source)
            try:
                text = recognizer.recognize_google(audio_data)
                full_text.append(text)
            except sr.UnknownValueError:
                full_text.append("[Unrecognized speech]")
            except sr.RequestError as e:
                full_text.append(f"[Error: {e}]")

        os.remove(chunk_path)  # Clean up the chunk file

    return "\n".join(full_text)

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        # Check if the file is uploaded
        if "file" not in request.files:
            return "No file part"
        file = request.files["file"]
        if file.filename == "":
            return "No selected file"
        
        # Save the uploaded file
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Extract audio from video
        audio_path = os.path.join(app.config['UPLOAD_FOLDER'], "temp_audio.wav")
        video = mp.VideoFileClip(file_path)
        video.audio.write_audiofile(audio_path)

        # Transcribe the audio to text
        transcription = transcribe_audio(audio_path)

        # Cleanup uploaded and temporary audio files
        os.remove(file_path)
        os.remove(audio_path)

        return render_template("result.html", transcription=transcription)
    
    return render_template("upload.html")

if __name__ == "__main__":
    app.run(debug=True)
