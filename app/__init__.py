import os
from flask import Flask, render_template, send_from_directory, Response, request
from dotenv import load_dotenv
from flask.typing import StatusCode
from werkzeug.sansio.response import Response
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from app.db import get_db
import subprocess

load_dotenv()
app = Flask(__name__)
app.config['DATABASE'] = os.path.join(os.getcwd(), 'flask.sqlite')
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html', title="Lance, Joe, Hamdia", url=os.getenv("URL"))

@app.route('/health')
def health():
    return "",200
