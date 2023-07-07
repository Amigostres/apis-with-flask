from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Reptile(db.Model):
    __tablename__ = "Reptiles"

    reptile_id = db.Column(db.Integer, primary_key = True)
    submitter = db.Column(db.String(255))
    information = db.Column(db.Text)
