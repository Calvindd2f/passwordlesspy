from flask import Blueprint, render_template, session, redirect, url_for, flash
from .passwordless_api import api_bp



bp = Blueprint('passwordless', __name__, url_prefix='/passwordless')

@bp.route('/')
def index():
    # Check if user is already authenticated
    if 'user_id' in session:
        # Redirect to a home or dashboard page if already logged in
        return redirect(url_for('dashboard'))
    
    return render_template('passwordless.html', title='Welcome to Passwordless Authentication')

@bp.route('/logout')
def logout():
    # Clear the session, logging the user out
    session.pop('user_id', None)
    flash('You have been logged out.')
    return redirect(url_for('.index'))

@bp.route('/dashboard')
def dashboard():
    # Dashboard or home page for authenticated users
    if 'user_id' not in session:
        flash('Please log in to access the dashboard.')
        return redirect(url_for('.index'))
    
    return render_template('dashboard.html', title='Your Dashboard')
