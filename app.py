import os
from flask import Flask, render_template, request, jsonify
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_URL = "https://judge0-ce.p.rapidapi.com/submissions?base64_encoded=false&wait=true"
API_KEY = os.getenv("JUDGE0_API_KEY")

HEADERS = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "judge0-ce.p.rapidapi.com",
    "Content-Type": "application/json"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/run", methods=["POST"])
def run_code():
    data = request.get_json()
    payload = {
        "language_id": data["language_id"],
        "source_code": data["source_code"],
        "stdin": data.get("stdin", "")
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)
    result = response.json()

    return jsonify({
        "stdout": result.get("stdout", ""),
        "stderr": result.get("stderr", ""),
        "time": result.get("time", "N/A"),
        "memory": result.get("memory", "N/A"),
        "status": result.get("status", {}).get("description", "Unknown")
    })

if __name__ == "__main__":
    app.run(debug=True)
