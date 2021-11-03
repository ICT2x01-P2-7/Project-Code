from flask import Flask, render_template, request
from flask.helpers import url_for
from werkzeug.utils import redirect
import hashlib

app = Flask(__name__) # Create the flask object  
 
@app.route('/')   
def default():  
    return render_template('index.html')

@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/connect.html', methods=['POST'])
def connect():
    error = "none"
    password = request.form.get('instructorPW')
    print(password)

    # Hash the password for comparison
    encoded = password.encode()
    result = hashlib.sha256(encoded)
    hexadecimal = result.hexdigest()

    print(hexadecimal)

    if hexadecimal != "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918":
        error = "Invalid password!"
        return redirect(url_for('home'))

    return render_template('connect.html', error=error)

@app.route('/game.html')
def game():
    return render_template('game.html')

@app.route('/challenge.html', methods=['POST'])
def challenge():
    addr = request.form.get("carIP")
    print(addr)
    return render_template('challenge.html')

@app.route('/upload.html')
def upload():
    global codeinput

    codeinput = request.file['code']

    # Code here uploads to car

    return render_template('upload.html')

if __name__ =='__main__':  
    app.run(debug = True)