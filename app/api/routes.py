"""API routes."""
from flask import jsonify, request
from app.api import bp
from app.models import User
from app.extensions import db


@bp.route('/health')
def health():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'message': 'Flask Starter Pack API is running'
    })


@bp.route('/version')
def version():
    """API version endpoint."""
    return jsonify({
        'version': '1.0.0',
        'name': 'Flask Starter Pack API'
    })


@bp.route('/test-user', methods=['POST'])
def create_test_user():
    """Create a test user for development."""
    # Check if user already exists
    if User.query.filter_by(username='testuser').first():
        return jsonify({
            'status': 'error',
            'message': 'Test user already exists'
        }), 400
    
    # Create test user
    user = User(username='testuser', email='test@example.com')
    user.set_password('password123')
    db.session.add(user)
    db.session.commit()
    
    return jsonify({
        'status': 'success',
        'message': 'Test user created successfully',
        'user': {
            'id': user.id,
            'username': user.username,
            'email': user.email
        }
    })


@bp.route('/users')
def list_users():
    """List all users (for development)."""
    users = User.query.all()
    return jsonify({
        'users': [{
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'is_active': user.is_active
        } for user in users]
    })


@bp.route('/echo', methods=['POST'])
def echo():
    """Echo endpoint for testing."""
    data = request.get_json()
    return jsonify({
        'message': 'Echo successful',
        'data': data
    })
