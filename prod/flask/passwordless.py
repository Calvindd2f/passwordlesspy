from flask import render_template

from .passwordless_api import api_bp
from .passwordless_bp import PasswordlessBlueprint

bp = PasswordlessBlueprint('passwordless', __name__, url_prefix='/passwordless')

@bp.route('/')
def index():
    # Check if user is already authenticated
    if 'user_id' in session:
        # Redirect to a home or dashboard page if already logged in
        return redirect(url_for('dashboard'))

    return render_template('passwordless.html', title='Welcome to Passwordless Authentication')

bp.register_blueprint(api_bp)

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



@bp.route('/api/create-token', methods=['GET'])
def create_token():
    email = request.args.get('email')
    if not email:
        return jsonify({'error': 'Email is required'}), 400

    # Integrate with Passwordless.dev to create a registration or login token
    token = generate_passwordless_token(email)

    return jsonify({'token': token})

@bp.route('/api/verify-login', methods=['GET'])
def verify_login():
    token = request.args.get('token')
    # Verify the token with Passwordless.dev's API
    # Establish a session or whatever is needed after verification
    return jsonify(success=True, userId='user_id')


@bp.route("/")
def index():
    return render_template(
        "passwordless.html",
        passwordless_api_url=bp.api_config.url,
        passwordless_api_key=bp.api_config.key,
    )
