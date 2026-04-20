from flask import Flask, render_template, jsonify
from monitor import get_system_health
from alerts import check_alerts
from datetime import datetime

app = Flask(__name__)

alert_history = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/health")
def health():
    data = get_system_health()
    alerts, status = check_alerts(data)

    for alert in alerts:
        alert_history.append({
            "message": alert,
            "time": datetime.now().strftime("%H:%M:%S")
        })

    return jsonify({
        "data": data,
        "alerts": alerts,
        "status": status,
        "history": alert_history[-10:]
    })

if __name__ == "__main__":
    app.run(debug=True)