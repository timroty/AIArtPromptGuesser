from flask import Flask

def create_app(config):
    # Create the Flask app
    app = Flask(__name__)

    # Configure the app
    app.config['DEBUG'] = config.debug

    # Initialize extensions (e.g., SQLAlchemy, JWT, etc.)
    # ...

    # Register blueprints and routes
    from app.routes import bp as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    # Set up database connections
    # ...

    return app
