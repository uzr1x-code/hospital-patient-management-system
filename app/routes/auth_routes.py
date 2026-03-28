from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash
from app import db
from app.models.user import User

auth = Blueprint('auth', __name__)

# Login Route
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('main.view_patients'))
        else:
            flash('Invalid username or password', 'danger')

    return render_template('login.html')

# Register Route
@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']

        user_exists = User.query.filter_by(username=username).first()
        if user_exists:
            flash('User already exists', 'danger')
            return redirect(url_for('auth.register'))

        hashed_password = generate_password_hash(password)

        user = User(username=username, password=hashed_password, role=role)
        db.session.add(user)
        db.session.commit()

        flash('Registration successful! Please login', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')

# Logout Route
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))