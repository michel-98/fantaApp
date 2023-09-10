import os

from dotenv import load_dotenv
from flask import Flask, render_template

import api_request
import matches_helper

app = Flask(__name__)
load_dotenv()


@app.route('/')
def index():
    return render_template('index.html')


# FC Braciollona
@app.route('/run', methods=['POST'])
def runUno():
    email_address = os.getenv("email_address")
    mailPassword = os.getenv("mailPassword")
    matchToken = os.getenv("matchToken")
    sergio = "michele.antonacasdsadasdassadasdasasdasci1098@gmail.com"
    antonello = os.getenv("antonello")
    fantaGoatPassword = os.getenv("fantaGoatPassword")

    print("matchToken" + matchToken)

    boolean = matches_helper.getIfTimeIsRunningUp(matchToken)
    if boolean:
        api_request.fetch_squadre_and_send_emails(email_address, mailPassword, fantaGoatPassword, sergio, antonello)
        return render_template('fatto.html')
    else:
        print("It's too soon")
        return render_template('soon.html')


# BET BET SIviglia
@app.route('/runDue', methods=['POST'])
def runDue():
    email_address = os.getenv("email_address")
    mailPassword = os.getenv("mailPassword")
    matchToken = os.getenv("matchToken")
    sergio = os.getenv("sergio")
    antonello = "michele.antonacasdsadasdassadasdasasdasci1098@gmail.com"
    fantaGoatPassword = os.getenv("fantaGoatPassword")

    print("matchToken" + matchToken)

    boolean = matches_helper.getIfTimeIsRunningUp(matchToken)
    if boolean:
        api_request.fetch_squadre_and_send_emails(email_address, mailPassword, fantaGoatPassword, sergio, antonello)
        return render_template('fatto.html')
    else:
        print("It's too soon")
        return render_template('soon.html')


if __name__ == "__main__":
    app.run()
