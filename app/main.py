from flask import Flask
import time
from prometheus_client import Counter, generate_latest
from prometheus_client import CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total number of requests"
)

@app.route("/")
def home():
    REQUEST_COUNT.inc()
    return {
        "status": "ok",
        "message": "API com métricas 🔥",
        "timestamp": int(time.time())
    }

@app.route("/health")
def health():
    return {"health": "UP"}

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
