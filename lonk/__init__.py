from flask import Flask
from flask_awscognito import AWSCognitoAuthentication
from flask_jwt_extended import JWTManager


# Globally accessable libraries
aws_auth = AWSCognitoAuthentication()
jwt_manager = JWTManager()


def create_app():
    app = Flask(__name__)

    #
    aws_auth.init_app(app)
    jwt_manager.init_app(app)

    app.config['SECRET_KEY'] = 'lonkes-awakening'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app

