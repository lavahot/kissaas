from random import choice, seed

from flask import render_template

from . import app

inspirations = [
    "Hang in there, baby.",
    "If at first you don't succeed, try again.",
    "You can do it. I know you can.",
    "Make your biggest dreams come true by working on its smallest parts.",
    "Fear is the mind-killer. Fear is the little-death that brings total obliteration. I will face my fear.",
    "You have more fans than you think.",
    "Do Better",
]


@app.route("/")
@app.route("/kindness")
def kindness(seed=seed()):
    return render_template("kindness.html", kindness=choice(inspirations))
