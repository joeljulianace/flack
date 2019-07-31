import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        error = None

        if not username:
            error = 'Username is required'

        if error is None:
            session.clear()
            print('==> Register Function')
            session['user_id'] = username
            user_id = session.get('user_id')
            print(f'User Id: {user_id}')
            return redirect(url_for('users.index'))                   

        flash(error)

    return render_template('auth/register.html')

@bp.before_app_request
def load_logged_in_user():
    print('==> Inside load_logged_in_user')
    user_id = session.get('user_id')
    print(f'User Id: {user_id}')
    if user_id is None:
        g.user = None
    else:
        g.user = user_id        

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.register'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.register'))

        return view(**kwargs)

    return wrapped_view    