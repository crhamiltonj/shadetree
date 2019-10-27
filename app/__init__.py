from flask import Flask


def create_app():
    app = Flask(__name__)

    from app.front.views import front_bp
    from app.admin.views import admin_bp

    with app.app_context():
        app.register_blueprint(front_bp)
        app.register_blueprint(admin_bp)

    return app
