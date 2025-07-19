from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

WEBHOOK_URL = "https://discord.com/api/webhooks/1395945977361465384/fMeIf8BwOf-VDuiAino5xmguCT8RSPZe4b8sm63DALNV0DJsDLep_EarlZurykZiBFK3"

@app.route("/api/send", methods=["POST"])
def send_webhook():
    data = request.get_json()
    username = data.get("username", "Roblox Player")
    
    content = f"🎮 Jogador **{username}** entrou no jogo!"
    
    try:
        r = requests.post(WEBHOOK_URL, json={"content": content})
        r.raise_for_status()
        return jsonify({"success": True}), 200
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
