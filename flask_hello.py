import requests
from flask import Flask

flask_application = Flask(__name__)

@flask_application.route('/')
def hello():
    return '<h1>AMD Hackathlon deadline is Sunday 12 July 2026 </h1>'
