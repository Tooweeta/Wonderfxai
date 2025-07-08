import os
import requests
from flask import Flask, request

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
# Either your user ID (e.g. 12345678) or a channel/username (e.g. "@TeresaFXAI_Bot")
CHAT_ID   = os.getenv("CHAT_ID")

@app.route('/webhook', methods=['POST'])
def webhook():
    data   = request.json or {}
    pair   = data.get("pair",   "UNKNOWN")
    action = data.get("action", "WAIT")
    price  = data.get("price",  "N/A")

    text = (
        f"📈 AI Forex Signal\n"
        f"Pair: {pair}\n"
        f"Signal: {action}\n"
        f"Price: {price}"
    )

    resp = requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json={"chat_id": CHAT_ID, "text": text}
    )
    # optional: log resp.status_code, resp.text
    return ("OK", 200) if resp.ok else (resp.text, resp.status_code)

if __name__ == "__main__":
    # Render requires host 0.0.0.0 and PORT env var
    port = int(os.getenv("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
