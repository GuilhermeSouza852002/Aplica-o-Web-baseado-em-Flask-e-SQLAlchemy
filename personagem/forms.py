from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import DataRequired

"""
id = db.Column(db.Integer, primary_key=True)
classe = db.Column(db.String(30), nullable=False)
hp = db.Column(db.Integer, nullable=False)
lv = db.Column(db.Integer, nullable=True)
forca = db.Column(db.Integer, nullable=True)
destreza = db.Column(db.Integer, nullable=True)
"""


class PersonagemForm(FlaskForm):
    id = IntegerField("Identificador", validators=[DataRequired()])
    classe = StringField("Classe do Personagem", validators=[DataRequired()])
    hp = IntegerField("Vida")
    lv = IntegerField("Level")
    forca = IntegerField("Força")
    destreza = IntegerField("Destreza")
