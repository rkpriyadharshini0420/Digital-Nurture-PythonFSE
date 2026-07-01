from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)

    # Import and register blueprints
    with app.app_context():
        from courses.routes import courses_bp
        from courses import models  # Ensure models are loaded for migration
        
        # Register the blueprint with the requested URL prefix
        app.register_blueprint(courses_bp, url_prefix='/api/courses')

    return app