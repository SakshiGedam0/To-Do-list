class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date=None):
        self.tasks.append({"description": description, "due_date": due_date, "completed": False})
        print(f"Task '{description}' added.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        for i, task in enumerate(self.tasks):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{i + 1}. {task['description']} - Due: {task['due_date']} - Status: {status}")

    def mark_complete(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
            print(f"Task '{self.tasks[task_index]['description']}' marked as complete.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            task = self.tasks.pop(task_index)
            print(f"Task '{task['description']}' deleted.")
        else:
            print("Invalid task number.")

    def update_task(self, task_index, new_description=None, new_due_date=None):
        if 0 <= task_index < len(self.tasks):
            if new_description:
                self.tasks[task_index]['description'] = new_description
            if new_due_date:
                self.tasks[task_index]['due_date'] = new_due_date
            print(f"Task '{self.tasks[task_index]['description']}' updated.")
        else:
            print("Invalid task number.")

def main():
    todo_list = TodoList()

    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Mark Complete\n4. Delete Task\n5. Update Task\n6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter task description: ")
            due_date = input("Enter due date (optional): ")
            todo_list.add_task(description, due_date)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_index = int(input("Enter task number to mark as complete: ")) - 1
            todo_list.mark_complete(task_index)
        elif choice == '4':
            task_index = int(input("Enter task number to delete: ")) - 1
            todo_list.delete_task(task_index)
        elif choice == '5':
            task_index = int(input("Enter task number to update: ")) - 1
            new_description = input("Enter new description (leave blank to keep current): ")
            new_due_date = input("Enter new due date (leave blank to keep current): ")
            todo_list.update_task(task_index, new_description, new_due_date)
        elif choice == '6':
            break
        else:
            print("Invalid option, please choose again.")

if __name__ == "__main__":
    main()
