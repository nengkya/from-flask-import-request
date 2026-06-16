import requests
from flask import Flask


#without flask_application = Flask(__name__) will be
#Error: Failed to find Flask application or factory in module 'flask_requests'. Use 'flask_requests:name' to specify one.
flask_application = Flask(__name__)


'''
without
@flask_application.route('/')
def hello():
    return '<h1> amd hackathlon deadline is sunday 12 july 2026 </h1>'

will be:
not found
the requested url was not found on the server. if you entered the url manually please check your spelling and try again.
'''

@flask_application.route('/')
def hello():
    return '<h1> AMD Hackathlon deadline is Sunday 12 July 2026 </h1>'


x = requests.get()
