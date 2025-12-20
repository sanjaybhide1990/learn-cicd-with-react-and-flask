# Application Factory

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()

def create_app(): 
    app = Flask(__name__)
    app.config.from_object(Config)

    # Add this to prevent 'MySQL server has gone away' errors
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
        "pool_recycle": 280,
        "pool_pre_ping": True,
    }

    db.init_app(app)

    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app