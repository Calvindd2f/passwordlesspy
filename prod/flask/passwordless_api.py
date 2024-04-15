from flask import Blueprint, request, jsonify, abort
from marshmallow import Schema, fields, validate, ValidationError

api_bp = Blueprint('passwordless_api', __name__, url_prefix='/api')

class LoginSchema(Schema):
    email = fields.Email(required=True)

@api_bp.route('/login', methods=['POST'])
def login():
    schema = LoginSchema()
    try:
        # Validate and deserialize input
        result = schema.load(request.get_json())
    except ValidationError as err:
        # Return a 400 response with the validation errors
        return jsonify({'errors': err.messages}), 400

    try:
        # Simulate API interaction
        # Here you would integrate with the passwordless.dev API
        # Placeholder for API client call, e.g., passwordless_client.login(email=result['email'])
        simulated_response = {"message": "Check your email for a login link", "status": "success"}
        return jsonify(simulated_response), 200
    except Exception as e:
        # Log the exception here
        return jsonify({'error': 'Internal server error', 'message': str(e)}), 500

@api_bp.errorhandler(404)
def handle_404(e):
    return jsonify({'error': 'Resource not found', 'message': str(e)}), 404

@api_bp.errorhandler(500)
def handle_500(e):
    return jsonify({'error': 'Internal server error', 'message': str(e)}), 500
