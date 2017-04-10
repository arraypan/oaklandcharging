import datetime

from flask import Flask, g, render_template, flash, redirect, url_for
from flask.ext.bcrypt import check_password_hash
from flask.ext.login import LoginManager, login_user, logout_user, login_required, current_user

import forms
import models

DEBUG = True
PORT = 8080
HOST = '0.0.0.0'

app = Flask(__name__)
app.secret_key = 'arrrpanfjanpcasdvmlasv'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == int(userid))
    except models.DoesNotExist:
        return None

@app.before_request
def before_request():
    g.db = models.DATABASE
    g.db.connect()
    g.user = current_user

@app.after_request
def after_request(response):
    g.db.close()
    return response

@app.route('/register', methods = ('GET', 'POST'))
def register():
    form = forms.RegisterForm()
    if form.validate_on_submit():
        models.User.create_user(
            email = form.email.data,
            phone = form.phone.data,
            password = form.password.data
        )
        flash("Thank you for registering!", "success")
        return redirect(url_for('index'))
    return render_template('register.html', form = form)

@app.route('/login', methods = ('GET', 'POST'))
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        try:
            user = models.User.get(models.User.email == form.email.data)
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                flash("Welcome, you're logged in!", "success")
                return redirect(url_for('index'))
            else:
                flash("The login was invalid.", "error")
        except models.DoesNotExist:
            flash("The login was invalid.", "error")
    return render_template('login.html', form = form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You're now logged out.", "success")
    return redirect(url_for('index'))

@app.route('/charge', methods=('GET', 'POST'))
@login_required
def charge():
    form = forms.ChargeForm()
    if form.validate_on_submit():
        models.Phone.create(
                            user = g.user._get_current_object(),
                            phone = form.phone.data.strip(),
                            email = form.email.data.strip(),
                            terms = form.terms.data,
                            id = form.id.data.strip()
                          )
        flash("Your Device has been Checked In. Thanks!", "success")
        return redirect(url_for('index'))
    return render_template('charge.html', form = form)

@app.route('/')
def index():
    tacos = models.Taco.select().limit(100)
    return render_template('index.html', charge=charge)


if __name__ == '__main__':
    models.initialize()
    app.run(debug = DEBUG, host = HOST, port = PORT)
