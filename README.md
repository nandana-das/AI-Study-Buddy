# 🎓 AI Learning Buddy

A Streamlit web app that acts as an AI-powered study buddy — enter any topic
and get a simple explanation, a real-life example, or a 5-question quiz,
generated instantly by Google's Gemini API.

## Features

- **Explain Concept** — plain-language explanation of any topic
- **Real-Life Example** — one relatable example tied to the topic
- **Generate Quiz** — 5 MCQs with answers
- **Ask Anything** — free-form question, including requesting feedback on
  a practice answer

## Run locally

```bash
git clone <your-repo-url>
cd <your-repo-folder>
pip install -r requirements.txt
```

Create `.streamlit/secrets.toml` (see `secrets.toml.example`) with your own
Gemini API key:

```toml
GEMINI_API_KEY = "your-gemini-api-key-here"
```

Get a free key at [aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey).

Then run:

```bash
streamlit run app.py
```

## Deploy on Streamlit Community Cloud

1. Push this repo to GitHub (make sure `.streamlit/secrets.toml` is **not**
   committed — it's covered by `.gitignore`).
2. Go to [share.streamlit.io](https://share.streamlit.io) and deploy from
   your repo, with `app.py` as the entry point.
3. In the app's **Settings → Secrets**, add:
   ```toml
   GEMINI_API_KEY = "your-gemini-api-key-here"
   ```
4. Deploy — you'll get a permanent `*.streamlit.app` link.

## Tech stack

Python · Streamlit · Google Gemini (`google-genai`)


## ⚠️ Security note

Never commit a real API key to this repo, in code or in `secrets.toml`.
If a key is ever exposed, regenerate it immediately at
[aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey).
