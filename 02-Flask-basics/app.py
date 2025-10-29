from flask import Flask # To create a Flask application
from flask import render_template # To render HTML templates
from flask_sqlalchemy import SQLAlchemy # For database handling
from datetime import datetime, timedelta, timezone # To handle date and time
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
    created = db.Column(db.DateTime, default=datetime.now(timezone.utc).astimezone(timezone(timedelta(hours=8))))  # When is is created

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


# Delete an Item
@app.route("/delete/<int:id>") # route for deleting a task by ID
def delete(id:int):
    delete_task = myTask.query.get_or_404(id) # Get the task by ID or return 404 if not found
    try:
        db.session.delete(delete_task) # Delete the task from the database session
        db.session.commit() # Commit the session to save changes
        return redirect('/') # Redirect to home page after deletion
    except Exception as e:
        print(f"ERROR: {e}")
        return f"ERROR: {e}" # Return error message if something goes wrong


# Edit an Item
@app.route("/edit/<int:id>", methods=['GET', 'POST']) # route for editing a task by ID
def edit(id:int):
    edit_task = myTask.query.get_or_404(id) # Get the task by ID or return 404 if not found
    if request.method == "POST":
        edit_task.content = request.form['content'] # Update the task content from form input
        try:
            db.session.commit() # Commit the session to save changes
            return redirect('/') # Redirect to home page after editing
        except Exception as e:
            print(f"ERROR: {e}")
            return f"ERROR: {e}" # Return error message if something goes wrong
    else:
        return render_template('edit.html', task=edit_task) # Render the edit.html template with the task to edit












if __name__ == '__main__':
    with app.app_context():
        db.create_all() # Create database tables
    
    app.run(debug=True) # To run and see the output in the browser