from flask import Blueprint

bp = Blueprint("qa", __name__, "/")

@bp.route("/")
def index():
    pass
