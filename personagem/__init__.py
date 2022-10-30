from flask import Blueprint

personagem_blueprint = Blueprint(
    "personagem_blueprint", __name__, url_prefix="/personagem")

from .routes import *
