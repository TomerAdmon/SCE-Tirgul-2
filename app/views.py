import os

from flask import render_template, flash, redirect, url_for, request, g
from flask import send_from_directory
from flask_login import login_user, logout_user, current_user, login_required

from app import app, login_manager
from .forms import LoginForm
from .models import User, Party


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def validateAndAdd(party_name):
    if (party_name == "AA"):
        flash('AA indeed.')
    pass


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'POST':
        validateAndAdd(request.form['party_name'])
        return redirect(url_for('login'))
    g.user = current_user
    parties = Party.query.all()
    return render_template('index.html',
                           title='Home',
                           user=g.user,
                           parties=parties)


@app.route('/admin')
@login_required
def admin():
    return render_template('a.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        form = LoginForm()
        if form.validate_on_submit():
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            user = User.query.filter_by(first_name=first_name).first()
            login_user(user)

            flash('Logged in successfully.')

            return redirect(url_for('index'))
        else:
            flash('Failed to log in.')
    return render_template('login.html', error=error)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/secret', methods=['GET'])
@login_required
def secret():
    return 'This is a secret page. You are logged in as {} {}'.format(current_user.first_name, current_user.last_name)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico', mimetype='image/vnd.microsoft.icon')