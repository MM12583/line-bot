from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,StickerSendMessage
)
from class_Draw import Draw

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



@handler.add(MessageEvent, message = TextMessage)
def handle_message(event):
    msg = event.message.text
    gift = Draw()
    if msg == '抽獎' :
        reply = '恭喜您抽中,' + str(gift.result)
        sticker_message = StickerSendMessage(package_id='11537', sticker_id='52002734')
        line_bot_api.reply_message(event.reply_token, sticker_message)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = reply))

if __name__ == "__main__": # 避免import時,直接執行 = main()
    app.run()