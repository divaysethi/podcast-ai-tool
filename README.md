# 🎧 Podcast AI Tool

> Transcribe and summarize podcast episodes using OpenAI Whisper and HuggingFace Transformers — fully local, offline, and scalable.

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Whisper](https://img.shields.io/badge/Whisper-OpenAI-green)
![Status](https://img.shields.io/badge/Build-Passing-brightgreen)

---

## 🧠 Overview

`podcast-ai-tool` is a Python-based tool that:
- 🎙️ **Records or accepts podcast audio**
- ✍️ **Transcribes** it using [OpenAI's Whisper](https://github.com/openai/whisper)
- 🧠 **Summarizes** transcripts using HuggingFace's Transformer models
- 🔁 Supports batch processing (handle 10+ podcasts at once)

Perfect for researchers, students, content creators, and productivity geeks.

---

## 🚀 Features

- 🎧 Record Spotify/system audio via virtual loopback
- 📁 Drop `.mp3` or `.wav` files into the `audio/` folder
- ✍️ Transcribes audio using `whisper`
- 🧠 Summarizes long transcripts into bite-sized insights
- 🗂 Saves all outputs in `transcripts/` and `summaries/`
- ✅ Fully offline support (optional cloud-based GPT available)

---

## 🛠️ Tech Stack

- Python 3.9+
- Whisper by OpenAI
- Transformers (HuggingFace)
- Torch, SoundDevice, Scipy

---

## 📦 Installation

```bash
git clone https://github.com/divaysethi/podcast-ai-tool.git
cd podcast-ai-tool
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

---

## 📝 Usage

### 🎙️ Record Audio
```bash
python record_audio.py
```

### ✍️ Transcribe All Files
```bash
python transcribe.py
```

### 🧠 Summarize Transcripts
```bash
python summarize.py
```

---

## 📁 Folder Structure

```
podcast-ai-tool/
├── audio/           # Drop your .mp3 or .wav podcast files here
├── transcripts/     # Auto-generated text transcripts
├── summaries/       # One-paragraph summaries of each episode
├── record_audio.py
├── transcribe.py
├── summarize.py
├── requirements.txt
└── README.md
```

---

## 💡 Future Enhancements

- [ ] Streamlit UI for drag-and-drop usage
- [ ] Auto keyword/tag extraction
- [ ] Export to Notion or Google Docs
- [ ] Merge summaries into one master report
