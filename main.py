from database import Base, engine
from cli import add_task, list_tasks, mark_done, delete_task

Base.metadata.create_all(engine)

def menu():
    print(""" it will print out the following menu:
TASK MANAGER
1. Add Task
2. View Tasks
3. Mark Task as Done
4. Delete Task
5. Exit
""")

def main():
    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
