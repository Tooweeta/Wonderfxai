from flask import Flask, request
import telegram
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telegram.Bot(token=BOT_TOKEN)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    pair = data.get("pair", "UNKNOWN")
    action = data.get("action", "WAIT")
    price = data.get("price", "N/A")
    message = f"📈 AI Forex Signal\nPair: {pair}\nSignal: {action}\nPrice: {price}"
    bot.send_message(chat_id="@YourChannelOrUserID", text=message)
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
