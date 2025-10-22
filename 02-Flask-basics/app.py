from flask import Flask # To create a Flask application
from flask import render_template # To render HTML templates
from flask_sqlalchemy import SQLAlchemy # For database handling
from datetime import datetime, timezone # To handle date and time
from flask import request, redirect # To handle form data and redirects

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

# Routes to Webpages
# Home page
@app.route('/', methods=['GET', 'POST']) # route for root URL
def home():

    # Add a new task
    if request.method == "POST":
        current_task = request.form['content'] # Get task content from form input
        new_task = myTask(content=current_task) # Create a new task instance
        try:
            db.session.add(new_task) # Add the new task to the database session
            db.session.commit() # Commit the session to save the task
            return redirect('/') # Redirect to home page after adding (updating the task list)
        except Exception as e:
            print(f"ERROR: {e}")
            return f"ERROR: {e}" # Return error message if something goes wrong
    # See all tasks
    else:
        tasks = myTask.query.order_by(myTask.created).all() # Getting all tasks ordered by when it was created
        return render_template('index.html', tasks=tasks) # Render the index.html template with tasks


if __name__ == '__main__':
    with app.app_context():
        db.create_all() # Create database tables
    
    app.run(debug=True) # To run and see the output in the browser