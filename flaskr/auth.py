import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('auth', __name__, url_defaults='/auth')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        display_name = request.form['displayname']
        error = None

        if not display_name:
            error = 'Display Name Is Required'
        
        if error is None:
            session.clear()
            session['user_id'] = display_name
            return redirect(url_for('index'))
        
        flash(error)
    
    return render_template('auth/register.html')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = user_id

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            redirect(url_for('index'))
        return view(**kwargs)
    
    return wrapped_view