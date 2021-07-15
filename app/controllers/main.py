from app import app, db

from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, login_required

from app.views.loginForm import LoginForm
from app.models.user import User
from app.views.registerForm import RegisterForm
from app.util.menu import Menu


@app.context_processor
def include_menu():
    return {'menu': Menu.items}


@app.route('/home')
@app.route('/')
@login_required
def home():
    return render_template('index.html', title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password', 'error')
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('home'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegisterForm()

    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully.', 'message')
        return redirect(url_for('login'))
    else:
        return render_template('self-register.html', form=form)
