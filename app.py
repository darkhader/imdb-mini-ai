from flask import Flask, request
from app_service import AppService
import json

app = Flask(__name__)
appService = AppService();


@app.route('/')
def home():
    return "App Works!!!"

@app.route('/api/<string:title>')
def get(title):
    return appService.get(title)

