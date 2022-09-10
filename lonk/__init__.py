from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm


# Globally accessable libraries
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)

    # aws_auth.init_app(app)
    # jwt_manager.init_app(app)

    # from .cognito import bp
    # app.register_blueprint(bp)

    from .views import views
    # from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    # app.register_blueprint(auth, url_prefix='/')

    @app.route("/")
    def test():
        return render_template("userview.html")

    return app

