from flask import Flask
from dotenv import load_dotenv
import os

def create_app():
    load_dotenv()  # loads the API key from '.env'
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = 'app/uploads'
    
    from app.routes import main
    app.register_blueprint(main)
    
    return app
