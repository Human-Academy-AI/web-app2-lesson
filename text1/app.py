# 必要なライブラリをインポート
from flask import Flask, render_template

# Flaskを使用する準備
app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/get_text", methods=["GET"])
def get_text_function():
    send_text = "私はgoogle colabです。"
    print("send_text={}".format(send_text))
    return send_text

@app.route("/")
def main():
    """トップページにアクセスしたときに実行される関数"""
    return render_template("index.html")

if __name__ == '__main__':
    app.run(port=5000)
