from flask import Flask, render_template, request
from flask.helpers import flash, url_for
from werkzeug.utils import redirect
from authenticate import check

app = Flask(__name__) # Create the flask object  
 
@app.route('/')   
def default():  
    return render_template('index.html')

@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/connect.html', methods=['POST'])
def connect():
    error = None
    password = request.form.get('instructorPW')
    print(password)

    result = check(password)

    if result:
        print(error)
        return render_template('connect.html', error=error)

    error = 'Invalid Password!'
    print(error)
    #return redirect(url_for('home', error=error))
    return render_template('index.html', error=error)

@app.route('/game.html', methods=['POST'])
def game():
    error = None
    difficulty = request.form.get("difficulty")
    print(difficulty)

    return render_template('game.html')

@app.route('/challenge.html', methods=['POST'])
def challenge():
    error = None
    addr = request.form.get("carIP")
    print(addr)

    check = validate_ip_address(addr)
    if check == False:
        error = 'Invalid IP Address!'
        return render_template('connect.html', error=error)

    return render_template('challenge.html')

def validate_ip_address(address):
    parts = address.split(".")

    if len(parts) != 4:
        print("IP address {} is not valid".format(address))
        return False

    for part in parts:
        if not isinstance(int(part), int):
            print("IP address {} is not valid".format(address))
            return False

        if int(part) < 0 or int(part) > 255:
            print("IP address {} is not valid".format(address))
            return False
 
    print("IP address {} is valid".format(address))
    return True 

@app.route('/upload.html')
def upload():
    global codeinput

    codeinput = request.file['code']

    # Code here uploads to car

    return render_template('upload.html')

if __name__ =='__main__':  
    app.run(debug = True)