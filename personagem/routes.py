from flask import render_template

from personagem import personagem_blueprint
from personagem.forms import PersonagemForm

from main import db

from model import Personagem


@personagem_blueprint.route("/", methods=["GET"])
def list_personagens():
    return render_template(
        template_name_or_list="personagem/list.html",
        personagens=Personagem.query.all())


@personagem_blueprint.route("/new", methods=["GET", "POST"])
def new_character():
    form = PersonagemForm()

    if form.validate_on_submit():
        personagem = Personagem(id=int(form.id.data), name=str(form.classe.data))
        db.session.add(personagem)
        db.session.commit()
        return "Personagem inserido com sucesso", 200

    return render_template("personagem/new.html", form=form)
