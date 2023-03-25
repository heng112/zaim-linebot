from dotenv import load_dotenv

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)

import json
import os
import sqlite3
import pandas as pd
from linebot import (LineBotApi, WebhookHandler)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage)
from linebot.exceptions import (LineBotApiError, InvalidSignatureError)


def lambda_handler():
    
    #環境変数として読み出し
    load_dotenv()
    LINE_ACCESS_TOKEN = os.getenv('LINE_ACCESS_TOKEN')
    LINE_USER_ID = os.getenv('LINE_USER_ID')


    #テキストの生成
    text = ""
    data =req_input('aaaaaaaawnwnwn')
    if(len(data) > 0):
        for item in data:
            text += f"{item['日付']} に {item['商品名']} を購入しています。\n"
            text += f"金額: {item['金額']}\n"
            text += f"お店: {item['お店']}\n\n"
    else:
        text = '購入履歴がありませんでした。'


    #message API
    line_bot_api = LineBotApi(channel_access_token=LINE_ACCESS_TOKEN )
    line_bot_api.push_message(LINE_USER_ID , TextSendMessage(text=text))

    return {
        'statusCode': 200,
        'body': json.dumps('ok', ensure_ascii=False)
    }

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

    
if __name__ == "__main__":
    print(lambda_handler())