from flask import Flask, render_template, request
from sequel import checker


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def Login():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        if checker(username,password)==0:
            return f"Welcome, {username}!"
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)#True,host='0.0.0.0',port=5000
    
