"""
Task Tracker - Full-Stack Flask Application
A simple task management web application with SQLite database
"""

from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

# Initialize Flask app
app = Flask(__name__)

# Database file path
DATABASE = 'database.db'


def get_db_connection():
    """
    Create and return a database connection.
    Creates the database file if it doesn't exist.
    """
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # This allows us to access columns by name
    return conn


def init_db():
    """
    Initialize the database by creating the tasks table if it doesn't exist.
    This function is called when the app starts.
    """
    conn = get_db_connection()
    # Create tasks table if it doesn't exist
    conn.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            completed INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()


@app.route('/')
def index():
    """
    Main route - displays all tasks and allows adding new tasks.
    """
    # Get database connection
    conn = get_db_connection()
    
    # Fetch all tasks from database
    tasks = conn.execute(
        'SELECT * FROM tasks ORDER BY id DESC'
    ).fetchall()
    
    conn.close()
    
    # Render the HTML template with tasks data
    return render_template('index.html', tasks=tasks)


@app.route('/add', methods=['POST'])
def add_task():
    """
    Route to handle adding a new task.
    Receives task name from form and saves it to database.
    """
    # Get task name from form
    task_name = request.form.get('task_name')
    
    # Only add if task name is not empty
    if task_name:
        conn = get_db_connection()
        # Insert new task into database (completed defaults to 0)
        conn.execute(
            'INSERT INTO tasks (name) VALUES (?)',
            (task_name,)
        )
        conn.commit()
        conn.close()
    
    # Redirect back to home page
    return redirect(url_for('index'))


@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    """
    Route to mark a task as completed.
    Updates the completed status in the database.
    
    Args:
        task_id: The ID of the task to mark as completed
    """
    conn = get_db_connection()
    # Update task's completed status to 1 (True)
    conn.execute(
        'UPDATE tasks SET completed = 1 WHERE id = ?',
        (task_id,)
    )
    conn.commit()
    conn.close()
    
    # Redirect back to home page
    return redirect(url_for('index'))


@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    """
    Route to delete a task from the database.
    
    Args:
        task_id: The ID of the task to delete
    """
    conn = get_db_connection()
    # Delete the task from database
    conn.execute(
        'DELETE FROM tasks WHERE id = ?',
        (task_id,)
    )
    conn.commit()
    conn.close()
    
    # Redirect back to home page
    return redirect(url_for('index'))


# Initialize database when app starts
if __name__ == '__main__':
    init_db()
    # Run the Flask app in debug mode (for development)
    app.run(debug=True)

