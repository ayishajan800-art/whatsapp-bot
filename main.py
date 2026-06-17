import requests
import flask
from flask import request, jsonify

# === یوازې دا 2 کرښې تا پخپله ډکولې ===
PHONE_NUMBER_ID = "117176209608179"  # ← ستا نمبر همدا دی
ACCESS_TOKEN = "EAAaZCEWoBx6IBRqoTnJ3e39qsjs4GEqEC2F5xp1ZBRvPnStNLvh7BnqT6G5Rcewp8xuWWQEbtZArmmc5HlRj7igDLdfJcY01xRx3PFHSe2zURoT1kZBoYLRa5VfNTRAD2ytiovJ4ZC85eZCN6jGAC5ZC8rSKKqvxDGNb4JaZAtEgVZBCZABGZAfRhZCLH0z3ZCQiVZCdIuNIclRdAyl0577i8iXpwdp1LcZCRheKc3A"
# =======================================

VERIFY_TOKEN = "my_verify_token_123"

app = flask.Flask(__name__)

@app.route("/webhook", methods=["GET"])
def verify():
    if request.args.get("hub.verify_token") == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return "Invalid"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    # دلته به د Gemini AI کوډ لګو
    return jsonify({"status": "ok"})

def send_message(to, text):
    url = f"https://graph.facebook.com/v20.0/{PHONE_NUMBER_ID}/messages"
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}", "Content-Type": "application/json"}
    data = {"messaging_product": "whatsapp", "to": to, "text": {"body": text}}
    requests.post(url, headers=headers, json=data)

if __name__ == "__main__":
    app.run(port=5000)
