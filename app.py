from flask import Flask, render_template, request
# from database import init_db
# import config
# import models.results
# from models.results import Result
# from sqlalchemy.sql import text
import datetime
import os

app = Flask(__name__)  # Flaskクラスのインスタンス生成

# app.config.from_object('config.Config')
# init_db(app)

luck = ["大凶", "大吉", "中吉", "小吉", "吉", "末吉", "末小吉", "凶", "小凶", "末凶"]


@app.route("/", methods=["GET"])
def get():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def post():
    now = datetime.datetime.today()  # 年～秒数まで取得する、呼び出すときは 変数名.year など
    timesum = now.year*now.month/now.day  # 日付までを入力値として使う

    age = request.form.get('age')  # ageという値をpostメソッド実行時にゲットする
    age = int(age)  # 受け取る値はstrなので計算ができるようintにキャスト

    r_id = request.form.get('sel')
    if r_id == None:
        # 入力値が初期値の場合の例外処理
        return render_template("index.html", message="項目を入力してください")
    r_id = int(r_id)

    result = timesum/(age+r_id) % 10   # 占いの結果を年齢と星座から求める

    # filter_by()で条件に一致するものを検索する、Resultのid内で一致するものをtesに格納してる
    # tes = Result.query.filter_by(id=result).first()

    # format()内の変数をmessageにある{}の中に挿入してる
    return render_template("index.html", message='あなたの今日の運勢は', message2=luck[result], message3='です')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
