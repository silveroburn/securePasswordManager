from flask import Flask, render_template, request
from sequel import checker, get_email ,chkuser,adduser
import requests
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

@app.route("/signup",methods=["GET","POST"])
def Signup():
    if request.method == "POST":
        username = request.form["username"]
        email=request.form["email"]
        password=request.form["password"]
        msg=chkuser(username,email)
        if msg:
            return render_template("signup.html",message=msg)
        else:
            adduser(username,email,password)
            return "User added successfull GOTO login page"
    
    return render_template("signup.html")

@app.route('/login', methods=['GET', 'POST'])
def Login():
    message=""
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        msg=checker(username,password)
        message=""
        if msg==0:
            return "Login successfull"
        elif msg==-2:
            message="Account Banned"
            data={"email": get_email(username)}
            response = requests.post('http://127.0.0.1:5000/mail',data=data)
            print(response.status_code)
            
            
        elif msg==-1:
            message="No Such Username"
        else:
            message=f"{msg} Tries Left"
    return render_template("home.html",message=message)

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
    app.run(debug=True)#True,host='0.0.0.0',port=5000