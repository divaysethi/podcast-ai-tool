import whisper
import os

model = whisper.load_model("base")
audio_dir = "audio"
output_dir = "transcripts"

os.makedirs(output_dir, exist_ok=True)

for file in sorted(os.listdir(audio_dir)):
    if file.endswith(".mp3") or file.endswith(".wav"):
        try:
            print(f"🔁 Transcribing {file}...")
            audio_path = os.path.join(audio_dir, file)
            result = model.transcribe(audio_path)

            # Clean filename for output
            base_name = os.path.splitext(file)[0].replace(" ", "_").lower()
            output_path = os.path.join(output_dir, f"{base_name}.txt")

            with open(output_path, "w", encoding="utf-8") as f:
                f.write(result["text"])

            print(f"✅ Transcribed: {file} → {output_path}")
        except Exception as e:
            print(f"❌ Error with {file}: {e}")
