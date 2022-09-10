from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return '<p>Login</p>'

@auth.route('/logout')
def logout():
    return '<p>Logout</p>'

@auth.route('/register')
def sign_up():
    return '<p>Sign Up!</p>'

@auth.route('/nonce')
def nonce():
    pass