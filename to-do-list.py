class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task_name, due_date=None):
        task_id = len(self.tasks) + 1
        self.tasks[task_id] = {"name": task_name, "due_date": due_date, "completed": False}
        print(f"Task '{task_name}' added successfully!")

    def view_tasks(self): 
        if not self.tasks:
            print("No tasks available!")
        else:
            print("Your To-Do List:")
            for task_id, task in self.tasks.items():
                status = "Completed" if task["completed"] else "Not Completed"
                print(f"{task_id}. {task['name']} - Due Date: {task['due_date']} - Status: {status}")

    def update_task(self, task_id, new_name=None, new_due_date=None):
        if task_id in self.tasks:
            if new_name:
                self.tasks[task_id]["name"] = new_name
            if new_due_date:
                self.tasks[task_id]["due_date"] = new_due_date
            print(f"Task {task_id} updated successfully!")
        else:
            print(f"Task {task_id} not found!")

    def delete_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
            print(f"Task {task_id} deleted successfully!")
        else:
            print(f"Task {task_id} not found!")

    def mark_completed(self, task_id):
        if task_id in self.tasks:
            self.tasks[task_id]["completed"] = True
            print(f"Task {task_id} marked as completed!")
        else:
            print(f"Task {task_id} not found!")


def main():
    todo = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_name = input("Enter task name: ")
            due_date = input("Enter due date (optional): ")
            todo.add_task(task_name, due_date)
        elif choice == "2":
            todo.view_tasks()
        elif choice == "3":
            task_id = int(input("Enter task ID: "))
            new_name = input("Enter new task name (optional): ")
            new_due_date = input("Enter new due date (optional): ")
            todo.update_task(task_id, new_name, new_due_date)
        elif choice == "4":
            task_id = int(input("Enter task ID: "))
            todo.delete_task(task_id)
        elif choice == "5":
            task_id = int(input("Enter task ID: "))
            todo.mark_completed(task_id)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()