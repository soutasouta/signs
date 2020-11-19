from flask import Flask, render_template, request
from database import init_db
import config
import models.results
from models.results import Result
from sqlalchemy.sql import text
import datetime

app = Flask(__name__)  # Flaskクラスのインスタンス生成

app.config.from_object('config.Config')
init_db(app)


@app.route("/", methods=["GET"])
def get():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def post():
    now = datetime.datetime.today()  # 年～秒数まで取得する、呼び出すときは 変数名.year など
    timesum = now.year+now.month+now.day  # 日付までを入力値として使う

    age = request.form.get('age')  # ageという値をpostメソッド実行時にゲットする
    age = int(age)  # 受け取る値はstrなので計算ができるようintにキャスト

    r_id = request.form.get('sel')
    if r_id == None:
        # 入力値が初期値の場合の例外処理
        return render_template("index.html", message="項目を入力してください")
    r_id = int(r_id)

    result = (age+r_id*timesum) % 10 + 10  # 占いの結果を年齢と星座から求める

    # filter_by()で条件に一致するものを検索する、Resultのid内で一致するものをtesに格納してる
    tes = Result.query.filter_by(id=result).first()

    # format()内の変数をmessageにある{}の中に挿入してる
    return render_template("index.html", message='あなたの今日の運勢は', message2=tes.f_result, message3='です')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
