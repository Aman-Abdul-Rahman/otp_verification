# Download the helper library from https://www.twilio.com/docs/python/install
import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from twilio.rest import Client
from tkinter import *


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


# Define Verify_otp() function
@app.route('/login' , methods=['POST'])
def verify_otp():
    username = request.form['username']
    password = request.form['password']
    mobile_number = request.form['number']

    if username == 'aman' and password == '5437':   
        account_sid = 'AC03da7138dbef63e97b81de5305edf004'
        auth_token = 'c189b593466167c19dc3d530e0cef2d1'
        client = Client(account_sid, auth_token)

        verification = client.verify \
            .services('VA7051aa16f77049653aac6d5880c1b73e') \
            .verifications \
            .create(to=mobile_number, channel='SMS')

        print(verification.status)
        return render_template('otp_verify.html')
    else:
        return render_template('user_error.html')



@app.route('/otp', methods=['POST'])
def get_otp():
    print('processing')

    received_otp = request.form['received_otp']
    mobile_number = request.form['number']

    account_sid = 'AC03da7138dbef63e97b81de5305edf004'
    auth_token = 'c189b593466167c19dc3d530e0cef2d1'
    client = Client(account_sid, auth_token)
                                            
    verification_check = client.verify \
        .services('VA7051aa16f77049653aac6d5880c1b73e') \
        .verification_checks \
        .create(to=mobile_number, code=received_otp)
    print(verification_check.status)

    if verification_check.status == "pending":
        return render_template('otp_error.html')    
    else:
        return redirect("https://project-c272.onrender.com/")


if __name__ == "__main__":
    app.run()

