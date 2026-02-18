from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "status": "ok",
        "message": "API rodando com sucesso 🚀",
        "timestamp": int(time.time())
    }

@app.route("/health")
def health():
    return {"health": "UP"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
