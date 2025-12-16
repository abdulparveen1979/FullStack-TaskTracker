# 📝 Task Tracker

A beginner-friendly full-stack web application for managing your daily tasks. Built with Python Flask, HTML, CSS, and SQLite database.

## ✨ Features

- ✅ **Add Tasks**: Create new tasks with a simple form
- 📋 **View Tasks**: See all your tasks in a clean, organized list
- ✓ **Complete Tasks**: Mark tasks as completed with a single click
- 🗑️ **Delete Tasks**: Remove tasks you no longer need
- 💾 **Persistent Storage**: All tasks are saved in SQLite database

## 🛠️ Tech Stack

- **Backend**: Python 3.x, Flask
- **Frontend**: HTML5, CSS3, Jinja2 Templates
- **Database**: SQLite3
- **Version Control**: Git & GitHub

## 📁 Project Structure

```
task-tracker/
├── app.py              # Flask backend application
├── requirements.txt    # Python dependencies
├── database.db         # SQLite database (created automatically)
├── README.md          # Project documentation
├── templates/
│   └── index.html     # Main HTML template
└── static/
    └── style.css      # CSS stylesheet
```

## 🚀 How to Run Locally

### Prerequisites

- Python 3.6 or higher installed on your system
- pip (Python package installer)

### Installation Steps

1. **Clone or download this repository**
   ```bash
   cd task-tracker
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open your browser**
   Navigate to `http://127.0.0.1:5000` or `http://localhost:5000`

## 📖 Usage

1. **Adding a Task**: Type your task in the input field and click "Add Task"
2. **Completing a Task**: Click the "✓ Complete" button next to any task
3. **Deleting a Task**: Click the "🗑️ Delete" button to remove a task permanently

## 🗄️ Database Schema

The application uses a SQLite database with the following structure:

**Table: tasks**
- `id` (INTEGER PRIMARY KEY AUTOINCREMENT) - Unique task identifier
- `name` (TEXT) - Task description
- `completed` (INTEGER) - Completion status (0 = not completed, 1 = completed)

## 🔧 API Routes

- `GET /` - Display all tasks and add task form
- `POST /add` - Add a new task
- `GET /complete/<id>` - Mark a task as completed
- `GET /delete/<id>` - Delete a task

## 🎯 Future Improvements

- [ ] User authentication and multiple user support
- [ ] Task categories and tags
- [ ] Due dates and reminders
- [ ] Task priority levels
- [ ] Search and filter functionality
- [ ] Export tasks to CSV/JSON
- [ ] Dark mode theme
- [ ] Task editing capability
- [ ] Drag and drop task reordering

## 📝 License

This project is open source and available for educational purposes.

## 👨‍💻 Author

Created as a beginner-friendly full-stack project.

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements!

---

**Happy Task Tracking! 🎉**

