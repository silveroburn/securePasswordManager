from flask import Flask, render_template, request
from sequel import checker

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
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
        elif msg==-1:
            message="No Such Username"
        else:
            message=f"{msg} Tries Left"
    return render_template("home.html",message=message)

if __name__ == "__main__":
    app.run(debug=True)#True,host='0.0.0.0',port=5000