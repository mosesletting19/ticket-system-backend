from flask import Flask
from flask_cors import CORS
from app.config import Config
from app.database import init_db
from app.routes import main_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)
    
    init_db(app)

    app.register_blueprint(main_bp)

    return app
