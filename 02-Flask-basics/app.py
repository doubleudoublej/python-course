from flask import Flask # To create a Flask application
from flask import render_template # To render HTML templates
from flask_sqlalchemy import SQLAlchemy # For database handling
from datetime import datetime, timezone # To handle date and time

app = Flask(__name__) # Initialize the Flask application
# simpliest and correct for most cases, have to change stuffs

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' # Database configuration
db = SQLAlchemy(app) # Initialize the database with the Flask app

# Data Class ~ Row of table
class myTask(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Primary key column
    content = db.Column(db.String(100), nullable=False) # Your actual task to do
    complete = db.Column(db.Boolean, default=False)  # Whether your task is completed
    created = db.Column(db.DateTime, default=datetime.now(timezone.utc))  # When is is created

    def __repr__(self):
        return f"Task {self.id}" 

@app.route('/') # route for root URL
def home():
    return render_template('index.html') # Render the index.html template

if __name__ == '__main__':
    with app.app_context():
        db.create_all() # Create database tables
    
    app.run(debug=True) # To run and see the output in the browser