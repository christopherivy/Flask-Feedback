from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


class User(db.Model):
    """fill this out"""

    __tablename__ = "users"  # should usually be plural

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.Text, nullable=False)  # need to add 20 char limit
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)  # need to add 50 char limit
    first_name = db.Column(db.Text, nullable=False)  # need to add 30 char limit
    last_name = db.Column(db.Text, nullable=False)  # need to add 30 char limit
