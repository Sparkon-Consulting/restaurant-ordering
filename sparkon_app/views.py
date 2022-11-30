from flask import Flask, render_template, url_for, request, redirect, flash, session
from . import app

import smtplib
import os
def send_email(name, email, message, subject):
    yahoopass = os.environ.get('MAIL_PASSWORD')
    my_email = os.environ.get('MAIL_USERNAME')
    server = os.environ.get('MAIL_SERVER')
    business_email = os.environ.get('BUSINESS_EMAIL')
    with smtplib.SMTP(server, port = 587) as connection:
        connection.starttls()
        connection.login(user = my_email, password = yahoopass)
        connection.sendmail(from_addr = my_email, to_addrs = business_email, msg = f"Subject: {subject}\n\n{name}\n{email} has sent you a message:\n\n{message}")


@app.route("/")
def home():
    return render_template('index.html',alicia_about=alicia_about,silent_partner_about=silent_partner_about)

@app.route("/aboutus")
def aboutus():
    return render_template('aboutus.html',about_us=about_us)

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/portfolio")
def portfolio():
    return render_template('portfolio.html')

@app.route("/services")
def services():
    return render_template('services.html')

@app.route("/message-sent", methods = ['GET','POST'])
def send_message():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        subject = request.form.get('subject')
        send_email(name, email, message, subject)
        return render_template('messagesent.html',message='Message sent!')
    return render_template('contact.html')

alicia_about = '''
Hi y'all, I have been coding in Python for the last 3 years and have fallen in love with technology
and the endless possibilities it offers. My goals are to enable others to truly leverage technology
to make their lives easier and more efficient.
'''

silent_partner_about = '''
Hello everyone I am a silent partner in this venture. I am an active engineer for 
a big tech company and have over 10 years of experience in the field. I look forward to helping
small businesses and individuals to leverage technology to optimize workflows and save time and money.
'''

about_us = '''
Hi everyone, we are a team of three engineers who have a passion for technology and helping others.
We initially started this venture as a clothing company to help spread awareness of Autism since our son is on the spectrum, who is 
non-verbal and constantly misunderstood. We have since expanded our offerings to include technology services because of our passion to help others.
Ultimately our goal is to provide FREE services and lessons to individuals and families who are on the spectrum or have some other form
of disability. We are proudly owned and operated by a Submarine Service Veteran out of the great state of Texas.
'''




if __name__ == "__main__":
    app.run()
