"""Main routes."""
from flask import render_template, flash, redirect, url_for
from app.main import bp


@bp.route('/')
@bp.route('/index')
def index():
    """Home page."""
    return render_template('main/index.html', title='Home')


@bp.route('/about')
def about():
    """About page."""
    return render_template('main/about.html', title='About')
