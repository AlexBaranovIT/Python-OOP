class Task:
    
    def __init__(self, task_name, priority):
        self.task_name = task_name
        self.priority = priority
        self.completed = False

    def complete(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"Task: {self.task_name}\nPriority: {self.priority}\nStatus: {status}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name, priority):
        task = Task(task_name, priority)
        self.tasks.append(task)

    def view_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                print(f"Task {index}:\n{task}\n")

    def complete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            task.complete()
            print(f"Task '{task.task_name}' marked as completed.")
        else:
            print("Invalid task index.")

    def remove_completed_tasks(self):
        self.tasks = [task for task in self.tasks if not task.completed]

    def __str__(self):
        return "\n".join([str(task) for task in self.tasks])


def main():
    print("Welcome to the To-Do List Manager!")

    todo_list = ToDoList()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Remove Completed Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_name = input("Enter task name: ")
            priority = input("Enter priority (Low, Medium, High): ").capitalize()
            todo_list.add_task(task_name, priority)

        elif choice == "2":
            print("\nYour To-Do List:")
            todo_list.view_tasks()

        elif choice == "3":
            task_index = int(input("Enter the task index to mark as completed: "))
            todo_list.complete_task(task_index)

        elif choice == "4":
            todo_list.remove_completed_tasks()
            print("Completed tasks removed.")

        elif choice == "5":
            print("Exiting the To-Do List Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

