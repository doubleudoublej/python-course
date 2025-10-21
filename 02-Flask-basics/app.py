from flask import Flask # To create a Flask application
from flask import render_template # To render HTML templates
from flask_sqlalchemy import SQLAlchemy # For database handling

app = Flask(__name__) # Initialize the Flask application
# simpliest and correct for most cases, have to change stuffs

@app.route('/') # route for root URL

def home():
    return render_template('index.html') # Render the index.html template

if __name__ == '__main__':
    app.run(debug=True) # To run and see the output in the browser