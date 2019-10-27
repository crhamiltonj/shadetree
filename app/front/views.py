from flask import Blueprint, render_template


front_bp = Blueprint(
    "front_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/front/static",
)


@front_bp.route("/")
def index():
    return render_template("index.html")

