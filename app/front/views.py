from flask import Blueprint, render_template, request


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


@front_bp.route('/signup', methods=['GET', 'POST'])
def register():
    return render_template('register.html')

@front_bp.route('/about')
def about():
    return render_template('about.html')

@front_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')
