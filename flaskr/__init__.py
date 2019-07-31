import os

from flask import Flask
from . import auth
from . import users

def create_app():
    app = Flask(__name__)
    app.secret_key = 'super secret key'


    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    app.register_blueprint(auth.bp)
    app.register_blueprint(users.bp)
    app.add_url_rule('/', endpoint='index')
    return app