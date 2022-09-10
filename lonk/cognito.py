from flask import Blueprint, url_for, request, redirect, make_response, render_template
from flask_jwt_extended import set_access_cookies, verify_jwt_in_request, get_jwt_identity

from . import aws_auth, jwt_manager

# 30 min cookie len
MAX_COOKIE_AGE = 30 * 60

bp = Blueprint('cognito', __name__)


@bp.route('/log_in/')
def log_in():
    return redirect(aws_auth.get_sign_in_url())


@bp.route('/logged_in/')
def logged_in():
    access_token = aws_auth.get_access_token(request.args)
    response = make_response(redirect(url_for("protected")))
    set_access_cookies(response, access_token, max_age=MAX_COOKIE_AGE)
    return response


@bp.route('/secret')
def protected():
    verify_jwt_in_request(optional=True)
    if get_jwt_identity():
        return render_template("secret.html")
    else:
        return redirect(aws_auth.get_sign_in_url())


