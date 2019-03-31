from flask import Flask, render_template
import os
import final

app = Flask(__name__)

@app.route('/')
def css():
    return render_template('mangrove.html')
	
@app.route('/location.html/')
def about():
    return render_template('location.html')

@app.route('/detect')
def detect():
    return final.main
	
if __name__ == '__main__':
	app.run(port = 3000)
	

	
