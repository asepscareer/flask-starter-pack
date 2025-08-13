"""Authentication routes."""
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app.auth import bp
from app.extensions import db
from app.models import User


@bp.route('/login', methods=['GET', 'POST'])
def login():
    """Login page."""
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        remember_me = bool(request.form.get('remember_me'))
        
        if not username or not password:
            flash('Please fill in all fields.', 'error')
            return render_template('auth/login.html', title='Sign In')
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user, remember=remember_me)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('main.index')
            flash(f'Welcome back, {user.username}!', 'success')
            return redirect(next_page)
        else:
            flash('Invalid username or password.', 'error')
    
    return render_template('auth/login.html', title='Sign In')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    """Registration page."""
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        
        # Validation
        if not all([username, email, password, password2]):
            flash('Please fill in all fields.', 'error')
            return render_template('auth/register.html', title='Register')
        
        if password != password2:
            flash('Passwords do not match.', 'error')
            return render_template('auth/register.html', title='Register')
        
        if len(password) < 6:
            flash('Password must be at least 6 characters long.', 'error')
            return render_template('auth/register.html', title='Register')
        
        # Check if user already exists
        if User.query.filter_by(username=username).first():
            flash('Username already exists.', 'error')
            return render_template('auth/register.html', title='Register')
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered.', 'error')
            return render_template('auth/register.html', title='Register')
        
        # Create new user
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('auth/register.html', title='Register')


@bp.route('/logout')
@login_required
def logout():
    """Logout user."""
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.index'))
