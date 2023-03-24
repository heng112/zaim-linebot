from dotenv import load_dotenv

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)

import json
import os
from linebot import (LineBotApi, WebhookHandler)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage)
from linebot.exceptions import (LineBotApiError, InvalidSignatureError)

# app = Flask(__name__)




def lambda_handler():
    
    #環境変数として読み出し
    load_dotenv()
    LINE_ACCESS_TOKEN = os.getenv('LINE_ACCESS_TOKEN')
    line_bot_api = LineBotApi(channel_access_token=LINE_ACCESS_TOKEN )
    line_bot_api.push_message("U370c2a0bea92c2a8b36ac821740510bd" , TextSendMessage(text='Hello World!'))

    return {
        'statusCode': 200,
        'body': json.dumps('ok', ensure_ascii=False)
    }

if __name__ == "__main__":
    print(lambda_handler())