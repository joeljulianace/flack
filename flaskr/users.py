import requests
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, session, jsonify
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required

bp = Blueprint('users', __name__)

@bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
   user_id = session.get('user_id')
   print('==>Index Function')
   print(f'User Id: {user_id}')
   if user_id is None:
       return redirect(url_for('auth.register'))
   else:
       return render_template('users/index.html')