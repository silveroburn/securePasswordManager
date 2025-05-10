from flask import Flask, request
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'sameer2020sameer123@gmail.com'
app.config['MAIL_PASSWORD'] = 'tujz rwda gthh sopm'  # Consider using env vars for security
app.config['MAIL_DEFAULT_SENDER'] = 'sameer2020sameer123@gmail.com'

mail = Mail(app)

@app.route('/mail', methods=['POST'])
def send_email():
    email = request.form.get("email")
    print(email)
    if not email:
        return "Email is required", 400

    msg = Message(
        'Hello',
        recipients=[email],
        body='Your account has been BANNED. Please contact Sameer Tiwary and Ashutosh Singh Naruka to lift the ban.'
    )

    try:
        mail.send(msg)
        print('Email sent successfully!')
        return "Email sent", 200
    except Exception as e:
        print(f"Error sending email: {e}")
        return "Failed to send email", 500

if __name__ == "__main__":
    app.run(debug=True)
