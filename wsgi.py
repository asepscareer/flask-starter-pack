"""
WSGI entry point for Flask Starter Pack production deployment.

Copyright (c) 2025 Asep Saputra
Licensed under the MIT License - see LICENSE file for details.
"""
import os
from app import create_app

# Get configuration from environment
config_name = os.environ.get('FLASK_CONFIG', 'production')
app = create_app()

if __name__ == "__main__":
    app.run()
