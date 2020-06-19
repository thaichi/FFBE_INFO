from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import os

app = Flask(__name__)

#環境変数取得
#YOUR_CHANNEL_ACCESS_TOKEN = os.environ["kLNPHyMUC36lYxo0ifRT/VjnLnVVEryoaEHt3mtYpeUeREmZgbdFmP0LfuLI5V6sfDCczeRxk3jKgwFUlOFctx5smZcL4SyXNuwG0P7jCAAOwu82sEwzB7Iq+Q87kakexnc1vQUfBHMn0k3u7k18LAdB04t89/1O/w1cDnyilFU="]
#YOUR_CHANNEL_SECRET = os.environ["5555a223a742ed7153d69462830b0c0b"]

line_bot_api = LineBotApi('kLNPHyMUC36lYxo0ifRT/VjnLnVVEryoaEHt3mtYpeUeREmZgbdFmP0LfuLI5V6sfDCczeRxk3jKgwFUlOFctx5smZcL4SyXNuwG0P7jCAAOwu82sEwzB7Iq+Q87kakexnc1vQUfBHMn0k3u7k18LAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('5555a223a742ed7153d69462830b0c0b')

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
