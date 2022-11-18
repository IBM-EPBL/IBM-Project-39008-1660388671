import email
from email import message
from importlib.resources import contents
from tkinter import S
from turtle import title
from flask import Flask,redirect, render_template, request, session, url_for, flash
from pyexpat import model
from sqlalchemy import PrimaryKeyConstraint
from werkzeug.utils import secure_filename
import ibm_db
from flask_mail import Mail, Message
from markupsafe import escape



app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=3883e7e4-18f5-4afe-be8c-fa31c41761d2.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31498;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=bvx19292;PWD=yDuuJH7Oqdzbnxnk;", "", "")
print(conn)
print("connection successful...")


# app.config['MAIL_SERVER']='smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = 'praveenmurugesan142001@gmail.com'
# app.config['MAIL_PASSWORD'] = '9486352215'
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True
# mail = Mail(app)


@app.route('/')
def home():
    return render_template('index.html',mes=message)




@app.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html')


@app.route('/signup', methods = ['GET','POST'])
def signup():
    return render_template('signup.html')

@app.route('/reqplasma', methods = ['GET','POST'])
def reqplasma():
    return render_template('plasmareq.html')


@app.route('/complaint')
def complaint():
    return render_template('complaint.html')


@app.route('/agentreg')
def agentreg():
    return render_template('agentreg.html')


@app.route('/agentlogin')
def agentlogin():
    return render_template('agentlogin.html')


@app.route('/agenthome')
def agenthome():
    return render_template('agenthome.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')



if __name__ == "__main__":
    app.run(debug=True)

