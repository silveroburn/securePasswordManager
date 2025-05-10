from flask import *
from flask_mail import Mail, Message
import requests

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'sameer2020sameer123@gmail.com'
app.config['MAIL_PASSWORD'] = 'tujz rwda gthh sopm'
app.config['MAIL_DEFAULT_SENDER'] = 'sameer2020sameer123@gmail.com'

mail = Mail(app)

@app.route('/mail', methods=['GET', 'POST'])
def send_email():
    if request.method == "POST":
        msg = Message(
            'Hello',
            recipients=['an7880@srmist.edu.in'],
            body='This is a test email sent from Flask-Mail!'
        )
        mail.send(msg)
        return 'Email sent successfully!'
    return "us cycle ki to maa chud gayi"

@app.route('/trigger', methods=['GET'])
def trigger_email():
    response = requests.post('http://127.0.0.1:5000/mail')
    return f'Triggered POST request. Response: {response.text}'

if __name__ == "__main__":
    app.run(debug=True)
