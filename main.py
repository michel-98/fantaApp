from flask import Flask, render_template
from dotenv import load_dotenv

import api_request
import matches_helper
import os

app = Flask(__name__)
load_dotenv()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/run', methods=['POST'])
def run():
    email_address = os.getenv("email_address")
    mailPassword = os.getenv("mailPassword")
    matchToken = os.getenv("matchToken")
    sergio = os.getenv("sergio")
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



if __name__ == "__main__":
    app.run()
