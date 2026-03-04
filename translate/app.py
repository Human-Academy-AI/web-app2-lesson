# 必要なライブラリをインポート
from flask import Flask, render_template,  jsonify, request
import boto3
import os

# Flaskを使用する準備
app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
app.config['TEMPLATES_AUTO_RELOAD'] = True

if 'AWS_SHARED_CREDENTIALS_FILE' not in os.environ:
  os.environ['AWS_SHARED_CREDENTIALS_FILE'] = '/content/.aws/credentials'
if 'AWS_CONFIG_FILE' not in os.environ:
  os.environ['AWS_CONFIG_FILE'] = '/content/.aws/config'

# --- ユーザー設定 ---
REGION_NAME = "ap-northeast-1"


@app.route("/translate", methods=["GET"])
def translate_function():
    """メッセージを貰って任意の処理を実行する関数"""
    # Webアプリ側から送られてきたテキストを取得する
    input_text = request.args.get("input_text")
    print("input_text={}".format(input_text))

    # AWSを使った翻訳の準備
    translate = boto3.client(service_name="translate",region_name=REGION_NAME)
    # テキストを翻訳
    translate_text = translate.translate_text(
        Text=input_text,
        SourceLanguageCode="ja",
        TargetLanguageCode="en"
    )["TranslatedText"]

    print("translate_text={}".format(translate_text))

    # Webアプリに翻訳したテキストを送り返す
    return translate_text

@app.route("/")
def main():
    """トップページにアクセスしたときに実行される関数"""
    return render_template("index.html")

if __name__ == '__main__':
    app.run(port=5002)
