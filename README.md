TaskMaster CLI  
A simple and efficient command-line task manager built using Python, SQLite, and SQLAlchemy ORM

 Overview
TaskMaster CLI is a lightweight productivity tool that helps users create, view, update, and delete tasks directly from the terminal.  
It uses SQLAlchemy to store tasks in a local SQLite database, ensuring all data is persistent and well-structured.

This project demonstrates:
- Python scripting  
- CLI interaction  
- Database integration  
- CRUD operations  
- Clean code architecture  

Technologies Used
-Python 3
SQLite (local file-based database)
SQLAlchemy ORM

Project Structure
task_manager/
│── main.py
│── cli.py
│── models.py
│── database.py
│── tasks.db (auto-created)
│── README.md
│── venv/ 


# Features (MVP)
✔ Add new tasks  
✔ View all tasks  
✔ Mark tasks as completed  
✔ Delete tasks  
✔ Persistent storage using SQLite  



#  User Stories
- As a user, I want to add tasks so I can keep track of what I need to do.  
- As a user, I want to view all my tasks so I can track my progress.  
- As a user, I want to mark tasks as completed so I know what I’ve finished.  
- As a user, I want to delete tasks so I can remove things I no longer need.  
# How to Run the Project

# 1. Clone the Repository
git clone https://github.com/Kilroy-creator/task_manager_cli.git
cd task_manager_cli

2. Create & Activate Virtual Environment

python3 -m venv 
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
3. Install Dependencies

pip install sqlalchemy

4. Run the App

python main.py

# Future Improvements

1. Add task deadlines

2. Add categories (work, personal, school)

3. Add color-coded CLI output

4. Export tasks to CSV or JSON

5. Add search/filter feature