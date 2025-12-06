from database import SessionLocal
from models import Task

session = SessionLocal()

def add_task():
    title = input("Enter task title: ")
    task = Task(title=title)
    session.add(task)
    session.commit()
    print("Task added successfully!")

def list_tasks():
    tasks = session.query(Task).all()
    if not tasks:
        print("No tasks found.")
    for t in tasks:
        print(f"{t.id}. {t.title} — {t.status}")

def mark_done():
    task_id = int(input("Enter task ID to mark as done: "))
    task = session.query(Task).get(task_id)
    if task:
        task.status = "Done"
        session.commit()
        print("Task marked as done.")
    else:
        print("Task not found.")

def delete_task():
    task_id = int(input("Enter task ID to delete: "))
    task = session.query(Task).get(task_id)
    if task:
        session.delete(task)
        session.commit()
        print("Task deleted.")
    else:
        print("Task not found.")
