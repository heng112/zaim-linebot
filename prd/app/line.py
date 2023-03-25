import os
from dotenv import load_dotenv
from waitress import serve
from flask import Flask, request, abort
import sqlite3
import pandas as pd

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

def req_input(input_str : str)-> list:
    
    conn = sqlite3.connect('../db/zaim.db')
    df = pd.read_sql(get_guery(shohin=input_str, filename="shohin.sql"), conn)
    result = df.to_dict(orient='records')
    return result


def get_guery(shohin: str, filename: str)->str:
    """
    SQLファイルに変数を挿入してクエリを作成する

    Args:
        num (int): 年齢
        category (str): 好きな果物
        filename (str): SQLファイルの名前

    Returns:
        str: SQLクエリ
    """
    with open(os.path.join("./sql/", filename), "r") as f:
        return f.read().format(shohin=shohin)


app = Flask(__name__)

#環境変数として読み出し
load_dotenv()
LINE_ACCESS_TOKEN = os.getenv('LINE_ACCESS_TOKEN')
LINE_CHANNEL = os.getenv('LINE_CHANNEL')


line_bot_api = LineBotApi(LINE_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL)

@app.route("/")
def hello_world():
    return 'OKk'

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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    #テキストの生成
    text = ""
    data =req_input(event.message.text)
    if(data[0] != ''):
        for item in data:
            text += f"{item['日付']} に {item['商品名']} を購入しています。\n"
            text += f"金額: {item['金額']}\n"
            text += f"お店: {item['お店']}\n\n"
    else:
        text = '購入履歴がありませんでした。'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=text))


if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=5000)