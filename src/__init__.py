import os

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials, storage

app = Flask(__name__)
CORS(app)

app_settings = os.getenv("APP_SETTINGS", "src.config.DevConfig")
app.config.from_object(app_settings)

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

firebase_credentials = credentials.Certificate(os.getenv("FIREBASE_CONFIG"))
firebase_admin.initialize_app(firebase_credentials, {
    "storageBucket": "thesis-recorder.appspot.com"
})
storage_bucket = storage.bucket()

from src.routers import auth_blueprint

app.register_blueprint(auth_blueprint)