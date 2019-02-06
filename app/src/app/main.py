# -*- coding:utf8 -*-
import site
site.addsitedir('utils')
site.addsitedir('controllers')

import os

from flask import Flask
from flask_cors import CORS

from helpers import hi_world
from http_controller import HttpController as http

app = Flask(__name__)
CORS(app)

hello_api = __import__('apis.hello.main', fromlist=['hello_api']).hello_api
app.register_blueprint(hello_api, url_prefix='/hello_world')

@app.route('/')
@http.response_json
def hello():
    node_name = os.environ.get('NODE_NAME', '')
    return [node_name, 'PID-: ', os.getpid(),os.getppid()], 3

if __name__ == "__main__":
    pass

