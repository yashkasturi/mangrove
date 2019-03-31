from flask import Flask, render_template
import os
import final

app = Flask(__name__)

@app.route('/')
def css():
    return "Mangrove"
	
@app.route('/location.html/')
def about():
    return render_template('location.html')

@app.route('/detect')
def detect():
    return final.main
	

	

	
