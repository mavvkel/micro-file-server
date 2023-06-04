from flask import Blueprint, redirect, render_template, request, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template(template_name_or_list='login.html')


@auth.route('/signup')
def signup():
    return render_template(template_name_or_list='signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    
    user = User.query.filter_by(email=email).first()
    if user:
        flash('Email address already registered')
        return redirect(url_for('auth.signup'))

    new_user = User(email=email,
                    name=name,
                    password=generate_password_hash(password=password,
                                                    method='sha256'))
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))


@auth.route('/logout')
def logout():
    return render_template(template_name_or_list='logout.html')
