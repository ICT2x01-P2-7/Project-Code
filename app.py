from flask import Flask, render_template

app = Flask(__name__) # Create the flask object  
 
@app.route('/')   
def default():  
    return render_template('index.html')

@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/advanced.html')
def advanced():
    return render_template('advanced.html')

@app.route('/beginner.html')
def beginner():
    return render_template('beginner.html')

@app.route('/statistics.html')
def statistics():
    return render_template('statistics.html')

if __name__ =='__main__':  
    app.run(debug = True)