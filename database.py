from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

# アプリでDB操作を行えるように初期設定する


def init_db(app):
    db.init_app(app)
    Migrate(app, db)
