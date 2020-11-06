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

app = Flask(__name__)

line_bot_api = LineBotApi('egkWrVC9KpxQMWybDUerIhxjdG9kA5zUW2STTQ1eJ8TsSY5rgX7XmjSFIa0kcY5oHmnwfy+5bF/j7gB3YQQu51CzGbn/YGPQvuZ37gdkFjZERyt+n3ejhddXZCKn55xTTtHXSR5JcD9Aa6jrEiW31QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('3dfdad77075487ac87d63c167136935a')


@app.route("/callback", methods=['POST']) # route 路徑 , '/callback' = 網址(伺服器) --> 連接 webhook
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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

count = 0

@handler.add(MessageEvent, message = TextMessage)
def handle_message(event):
    msg = event.message.text
    reply = '我是機器人，現在起會和您說同樣的話'
    if msg == 'reset' :
        count = 0 
    if count == 0 :
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = reply,msg))
    if count <= 3 :
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = msg))
    elif count <= 5 :
        reply = '您很閒是吧'
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = reply))
    elif count == 6 :
        reply = '好吧，完最後一次'
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = reply))
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = msg))
    elif count == 7 :
        reply = '我累了，掰撲'
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = reply))
    else :
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = None))
    count += 1 

if __name__ == "__main__": # 避免import時,直接執行 = main()
    app.run()