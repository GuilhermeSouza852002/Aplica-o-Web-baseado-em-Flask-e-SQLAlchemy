from main import db
from datetime import datetime


class Personagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    classe = db.Column(db.String(30), nullable=False)

    created = db.Column(db.String(15), nullable=False,
                        default=str(datetime.utcnow()))

    hp = db.Column(db.Integer, nullable=True)

    lv = db.Column(db.Integer, nullable=True)

    forca = db.Column(db.Integer, nullable=True)

    destreza = db.Column(db.Integer, nullable=True)
