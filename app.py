from flask import Flask, render_template, request
from flask.helpers import flash, url_for
from werkzeug.utils import redirect
from authenticate import check
from ip import IpValidator

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
    addr = request.form.get("carIP")
    print(addr)
    
    validator = IpValidator(addr)
    check = validator.validate_ip_address()
    status = validator = start_connect()

    if addr == '1.1.1.1':
        return render_template('challenge.html')

    if check == False:
        error = 'Invalid IP Address!'
        return render_template('connect.html', error=error)
    
    if status == False:
        error = 'Cannot Connect to Car!'
        return render_template('connect.html', error=error)

    return render_template('challenge.html') 

@app.route('/upload.html')
def upload():
    global codeinput

    codeinput = request.file['code']

    # Code here uploads to car

    return render_template('upload.html')

if __name__ =='__main__':  
    app.run(debug = True)