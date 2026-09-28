from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Cerebro Ippon Webhook funcionando!", 200

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        verify_token = "cerebro_ippon_2026"
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if mode == "subscribe" and token == verify_token:
            return challenge, 200

        return "Falha na verificacao", 403

    if request.method == "POST":
        dados = request.get_json()
        print(dados)
        return "EVENT_RECEIVED", 200
