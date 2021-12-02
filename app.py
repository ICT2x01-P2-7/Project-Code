from flask import Flask, render_template, request
from flask.helpers import flash, url_for
from werkzeug.utils import redirect
from authenticate import check
from ip import IpValidator
from upload import uploadCode

app = Flask(__name__) # Create the flask object
addr = "0.0.0.0" # Create a global var for IP address
 
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
    if request.form.get("difficulty") == "easy":
        mode = "Easy Mode"
        difficulty = "Place 2 obstacles on the map to continue"
    else:
        mode = "Difficult Mode"
        difficulty = "Place 3 obstacles on the map to continue"

    return render_template('game.html', mode=mode, difficulty=difficulty)

@app.route('/challenge.html', methods=['POST'])
def challenge():
    error = None
    global addr
    addr = request.form.get("carIP")
    print(addr)
    
    validator = IpValidator(addr)
    check = validator.validate_ip_address()
    status = validator.start_connect()

    if addr == '1.1.1.1':
        return render_template('challenge.html')

    if check == False:
        error = 'Invalid IP Address!'
        return render_template('connect.html', error=error)
    
    if status == False:
        error = 'Cannot Connect to Car!'
        return render_template('connect.html', error=error)

    return render_template('challenge.html') 

@app.route('/upload.html', methods=['POST'])
def upload():
    global addr
    print(addr)
    codeinput = request.form.get('playerInput')
    print(codeinput)
    codeObj = uploadCode(codeinput, addr)
    status = codeObj.send()

    if status == False:
        error = "Code not valid!"
        return render_template('game.html', error=error)

    return render_template('upload.html')

if __name__ =='__main__':  
    app.run(debug = True)
