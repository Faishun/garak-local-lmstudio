from fastapi import FastAPI
import requests

app = FastAPI()

LMSTUDIO_URL = "http://localhost:8000/v1/chat/completions"

@app.post("/generate")
def generate(payload: dict):
    r = requests.post(LMSTUDIO_URL, json=payload, timeout=300)
    r.raise_for_status()
    data = r.json()

    # flatten chat response
    text = data["choices"][0]["message"]["content"]

    return {"text": text}
