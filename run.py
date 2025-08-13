#!/usr/bin/env python3
"""
Development server runner for Flask Starter Pack.

Copyright (c) 2025 Asep Saputra
Licensed under the MIT License - see LICENSE file for details.
"""
import os
from app import create_app

if __name__ == '__main__':
    os.environ.setdefault('FLASK_ENV', 'development')
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=8080)
