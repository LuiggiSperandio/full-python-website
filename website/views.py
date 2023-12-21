from flask import Blueprint, render_template, redirect
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/redirect')
def test_redirect():
    return render_template('redirect_temp.html', user=current_user)