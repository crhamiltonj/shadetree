from flask import Flask


def create_app():
    app = Flask(__name__)

    from app.front.views import front_bp

    with app.app_context():
        app.register_blueprint(front_bp)

    return app
