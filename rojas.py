from rojaslab import app
from flask import render_template, session, request, redirect, url_for, flash, abort
from flask_login import login_user, login_required, logout_user
from flask_mail import Message
from werkzeug.utils import secure_filename
import os

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')



if __name__ == '__main__':
    app.run(debug=True)