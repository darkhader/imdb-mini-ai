from flask import Flask, request
from flask_cors import CORS, cross_origin
from app_service import AppService
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
appService = AppService();


@app.route('/')
@cross_origin(supports_credentials=True)
def home():
    return "App Works!!!"

@app.route('/api', methods = ['POST'])
@cross_origin(supports_credentials=True)
def get():
    title = request.form['title']
    return appService.get(title)

