from database import db


class Result(db.Model):
    __tablename__ = 'results'  # table名は複数形で書くのが常識らしい

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    f_result = db.Column(db.String(45), nullable=False)
