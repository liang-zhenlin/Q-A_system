from flask import Blueprint

qa = Blueprint("qa", __name__, "/")

@qa.route("/")
def index():
    pass
