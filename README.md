# Flask Starter Pack

[![Deploy on Railway](https://railway.com/button.svg)](https://railway.com/deploy/flask-starter-pack-1?referralCode=asepsp)

A clean and organized Flask application starter template with authentication, blueprints, and modern UI components.

## 🚀 Features

- **✅ Blueprint Organization**: Separate modules for main, auth, and API functionality
- **✅ Authentication System**: Complete login/registration with Flask-Login and User model
- **✅ Database Integration**: SQLAlchemy ORM with migrations and User model implemented
- **✅ Modern UI**: Bootstrap 5 with responsive design and custom components
- **✅ API Ready**: RESTful endpoints with JSON responses and health checks
- **✅ Form Handling**: Working registration and login forms with validation
- **✅ Error Handling**: Custom 404 and 500 error pages
- **✅ Configuration Management**: Environment-based configuration with .env support
- **✅ Production Ready**: Gunicorn WSGI server configuration
- **✅ Railway Deployment**: Ready for Railway.app deployment

## 📁 Project Structure

```
flask-starter-pack/
├─ app/
│  ├─ __init__.py           # Flask app factory with user_loader
│  ├─ config.py            # Configuration classes
│  ├─ extensions.py        # Flask extensions (db, migrate, login_manager)
│  ├─ models.py            # User model with authentication
│  ├─ main/                # Main blueprint
│  │  ├─ __init__.py
│  │  └─ routes.py         # Home, about routes
│  ├─ auth/                # Authentication blueprint  
│  │  ├─ __init__.py
│  │  └─ routes.py         # Login, register, logout routes
│  ├─ api/                 # API blueprint
│  │  ├─ __init__.py
│  │  └─ routes.py         # Health, version, users API
│  ├─ templates/           # Jinja2 templates
│  │  ├─ base.html         # Base template with Bootstrap
│  │  ├─ main/             # Main page templates
│  │  │  ├─ index.html
│  │  │  └─ about.html
│  │  ├─ auth/             # Auth page templates
│  │  │  ├─ login.html
│  │  │  └─ register.html
│  │  ├─ errors/           # Error page templates
│  │  │  ├─ 404.html
│  │  │  └─ 500.html
│  │  ├─ partials/         # Reusable components
│  │  │  ├─ _navbar.html
│  │  │  ├─ _footer.html
│  │  │  └─ _flash.html
│  │  └─ macros/           # Jinja2 macros
│  │     ├─ forms.html
│  │     └─ components.html
│  └─ static/              # Static assets
│     ├─ css/app.css       # Custom CSS
│     ├─ js/app.js         # Custom JavaScript
│     └─ img/              # Images
├─ migrations/             # Database migrations
├─ instance/               # Instance folder (gitignored)
├─ .env                    # Environment variables (gitignored)
├─ .gitignore             # Git ignore rules
├─ wsgi.py                 # WSGI entry point
├─ run.py                  # Development server runner
├─ requirements.txt        # Python dependencies
├─ railway.json           # Railway deployment config
├─ LICENSE                # MIT License
└─ README.md
```

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd flask-starter-pack
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set environment variables**
   Create a `.env` file in the root directory:
   ```env
   SECRET_KEY=your-secret-key-here
   FLASK_APP=wsgi.py
   FLASK_ENV=development
   DATABASE_URL=sqlite:///app.db
   ```

5. **Initialize database**
   ```bash
   flask db init        # Already done - creates migrations folder
   flask db migrate -m "Initial migration with User model"  # Already done
   flask db upgrade     # Already done - creates tables
   ```

6. **Run the application**
   ```bash
   flask run
   # Or for development with auto-reload:
   python run.py
   ```

7. **Test the application**
   - Homepage: http://127.0.0.1:5000
   - Register: http://127.0.0.1:5000/auth/register  
   - Login: http://127.0.0.1:5000/auth/login
   - API Health: http://127.0.0.1:5000/api/health

## 🔧 Configuration

The application supports multiple configuration environments:

- **Development**: Debug mode enabled, SQLite database, detailed error messages
- **Production**: Debug disabled, secure cookies, production database  
- **Testing**: In-memory database, CSRF disabled, fast testing

**Environment Variables (.env file):**
```env
SECRET_KEY=your-secret-key-here
FLASK_APP=wsgi.py  
FLASK_ENV=development
DATABASE_URL=sqlite:///app.db
```

**Set Configuration Environment:**
```bash
export FLASK_CONFIG=development  # or production, testing
flask run
```

## 📝 Usage

### 🔐 Authentication System

The application includes a complete authentication system:

**User Registration:**
```bash
# Visit: http://127.0.0.1:5000/auth/register
# Required fields: username, email, password, confirm password
```

**User Login:**
```bash
# Visit: http://127.0.0.1:5000/auth/login  
# Required fields: username, password
# Optional: remember me checkbox
```

**User Model Features:**
- Password hashing with Werkzeug
- Flask-Login integration
- Unique username and email validation
- Active user status tracking

### 🗄️ Database Operations

**Access Flask Shell:**
```bash
flask shell
>>> from app.models import User
>>> from app.extensions import db

# Create a user programmatically
>>> user = User(username='admin', email='admin@example.com')
>>> user.set_password('admin123')
>>> db.session.add(user)
>>> db.session.commit()

# Query users
>>> users = User.query.all()
>>> user = User.query.filter_by(username='admin').first()
>>> print(user.email)
```

### 🔌 API Endpoints

The application provides several API endpoints:

**Health Check:**
```bash
GET /api/health
# Response: {"status": "healthy", "message": "Flask Starter Pack API is running"}
```

**Version Info:**
```bash
GET /api/version  
# Response: {"version": "1.0.0", "name": "Flask Starter Pack API"}
```

**User Management:**
```bash
GET /api/users
# Response: {"users": [{"id": 1, "username": "testuser", "email": "test@example.com", "is_active": true}]}

POST /api/test-user
# Creates a test user for development
```

### 📄 Adding New Blueprints

1. Create a new directory in `app/`
2. Add `__init__.py` with blueprint definition:
```python
from flask import Blueprint
bp = Blueprint('new_module', __name__)
from app.new_module import routes
```
3. Create `routes.py` with route handlers
4. Register the blueprint in `app/__init__.py`:
```python
from app.new_module import bp as new_module_bp
app.register_blueprint(new_module_bp, url_prefix='/new_module')
```

### 🎨 Template Structure

Templates are organized hierarchically:
- `base.html` - Main layout with Bootstrap
- `partials/` - Reusable components (navbar, footer, flash messages)
- `main/` - Homepage and about page templates  
- `auth/` - Login and registration templates
- `errors/` - Custom error page templates

### Using Macros

The starter pack includes useful Jinja2 macros in `templates/macros/`:
```html
{% from 'macros/forms.html' import render_field %}
{% from 'macros/components.html' import alert, card %}

{{ render_field(form.email) }}
{{ alert('Success message', 'success') }}
```

## 🚀 Deployment

### Railway.app

This starter pack is ready for deployment on Railway:

1. Connect your GitHub repository to Railway
2. Set environment variables in Railway dashboard
3. Deploy automatically on push to main branch

### Manual Deployment

1. **Set production environment variables**
2. **Install dependencies**: `pip install -r requirements.txt`
3. **Run with Gunicorn**: `gunicorn wsgi:app`

## 🔒 Security Features

- CSRF protection on all forms
- Secure session cookies
- SQL injection prevention with SQLAlchemy
- XSS protection with Jinja2 auto-escaping
- Security headers with Flask-Talisman (optional)

## 🎨 Customization

### Styling

- Modify `app/static/css/app.css` for custom styles
- Bootstrap 5 classes available throughout templates
- CSS custom properties defined for consistent theming

### JavaScript

- Custom utilities available in `window.FlaskApp`
- Bootstrap components initialized automatically
- AJAX helper functions included

## 📚 API Endpoints

The starter pack includes these working API endpoints:

**Core Endpoints:**
- `GET /api/health` - Application health check
- `GET /api/version` - API version information  
- `GET /api/users` - List all registered users (development)
- `POST /api/test-user` - Create test user (development)

**Example API Usage:**
```bash
# Test health endpoint
curl http://127.0.0.1:5000/api/health

# Create test user
curl -X POST http://127.0.0.1:5000/api/test-user

# List users  
curl http://127.0.0.1:5000/api/users
```

## � Testing

### Quick Test Checklist

**✅ Application Startup:**
```bash
flask run
# Should start without errors on http://127.0.0.1:5000
```

**✅ Core Pages:**
- Homepage: http://127.0.0.1:5000 ✅
- About: http://127.0.0.1:5000/about ✅  
- Login: http://127.0.0.1:5000/auth/login ✅
- Register: http://127.0.0.1:5000/auth/register ✅

**✅ API Endpoints:**
- Health: http://127.0.0.1:5000/api/health ✅
- Version: http://127.0.0.1:5000/api/version ✅
- Users: http://127.0.0.1:5000/api/users ✅

**✅ Authentication Flow:**
1. Register new user via form
2. Login with registered credentials  
3. Verify navbar shows logout option
4. Test logout functionality

**✅ Database:**
```bash
flask shell
>>> from app.models import User
>>> User.query.count()  # Should show registered users
```

## �🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Copyright (c) 2025 Asep Saputra**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

## 🆘 Support

If you encounter any issues or have questions:

1. Check the documentation
2. Search existing issues
3. Create a new issue with detailed information

## 🙏 Acknowledgments

**Author:** Asep Saputra  
**Created:** August 2025  
**Flask Starter Pack** - A comprehensive template for modern Flask applications

**Special Thanks:**
- Flask and its ecosystem for the amazing framework
- Bootstrap team for the beautiful UI components  
- Railway.app for the excellent hosting platform
- Python community for continuous innovation

**Technology Stack:**
- Python 3.8+
- Flask 2.3+
- SQLAlchemy & Flask-Migrate
- Flask-Login for authentication
- Bootstrap 5 for responsive UI
- Jinja2 templating engine
