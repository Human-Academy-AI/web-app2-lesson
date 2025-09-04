#!/usr/bin/env python3

# 必要なライブラリをインポート
from flask import Flask, render_template, request

# Flaskを使用する準備
app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0


@app.route("/send", methods=["GET"])
def send_function():
    # Webアプリから受け取ったテキストを取り出す
    input_text = request.args.get("text")
    send_text = "「{}」というメッセージを受け取ったよ！".format(input_text)
    
    print("input_text={}".format(input_text))
    print("send_text={}".format(send_text))
    return send_text
    

@app.route("/")
def main():
    """トップページにアクセスしたときに実行される関数"""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)