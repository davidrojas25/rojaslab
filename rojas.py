from rojaslab import app, mail
from rojaslab.forms import ContactUsForm
from flask import render_template, session, request, redirect, url_for, flash, abort, send_from_directory
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

@app.route('/contactus', methods=['GET', 'POST'])
def contactus():
    
    form = ContactUsForm()
    
    if form.validate_on_submit():
        session['first'] = form.first.data
        session['last'] = form.last.data
        session['email'] = form.email.data
        session['phonenum'] = form.phonenum.data
        session['message'] = form.message.data
        msg = Message('New Warrior Contact Us Message', recipients=['wareliteracing@gmail.com'], reply_to=session['email'])
        msg.body = session['message']
        if form.file.data != None:
            file = form.file.data
            filename = secure_filename(form.file.data.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            with app.open_resource(os.path.join(app.config['UPLOAD_FOLDER'], filename)) as fp:
              msg.attach(filename, "image/png", fp.read())
        mail.send(msg)
        
        flash('Thanks for the Message! We will get back to you soon!')
        return redirect(url_for('thankyou'))
        
    return render_template('contactus.html', form=form)

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

@app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])



if __name__ == '__main__':
    app.run(debug=True)