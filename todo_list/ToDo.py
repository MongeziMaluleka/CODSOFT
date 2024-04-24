import tkinter as tk
from tkinter import messagebox, simpledialog

class ToDoList:
    """Class representing a simple to-do list."""
    
    def __init__(self):
        # Initialize the ToDoList class with an empty list of tasks.
        self.tasks = []

    def add_task(self, task):
        # Add a new task to the list of tasks.
        self.tasks.append(task)

    def update_task(self, index, new_task):
        # Update an existing task at a specific index if the index is valid.
        if 0 <= index < len(self.tasks):
            self.tasks[index] = new_task
            return True
        return False

    def delete_task(self, index):
        # Delete a task at a specific index if the index is valid.
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            return True
        return False

    def get_tasks(self):
        # Return the current list of tasks.
        return self.tasks

class App:
    """Main Application class managing different screens."""
    
    def __init__(self, root):
        # Initialize the app with the main tkinter window (root) and a ToDoList.
        self.root = root
        self.todo_list = ToDoList()
        self.main_window()

    def main_window(self):
        """Create the main window with buttons for task operations."""
        # Set the title and size of the window.
        self.root.title("To-Do List Application")
        self.root.geometry("300x250")

        # Create buttons for various task operations and pack them into the window.
        tk.Button(self.root, text="View Tasks", command=self.view_tasks).pack(fill='x')
        tk.Button(self.root, text="Create Task", command=self.create_task).pack(fill='x')
        tk.Button(self.root, text="Update Task", command=self.update_task).pack(fill='x')
        tk.Button(self.root, text="Delete Task", command=self.delete_task).pack(fill='x')

    def view_tasks(self):
        """Display all tasks in a message box."""
        tasks_str = "\n".join(f"{i}. {task}" for i, task in enumerate(self.todo_list.get_tasks(), 1))
        messagebox.showinfo("View Tasks", tasks_str or "No tasks available.")

    def create_task(self):
        """Create a new task via a dialog box."""
        task_description = simpledialog.askstring("Create Task", "Enter Task Description:")
        if task_description and task_description.strip():
            self.todo_list.add_task(task_description.strip())
            messagebox.showinfo("Success", "Task added successfully.")

    def update_task(self):
        """Update an existing task via a dialog box."""
        index = simpledialog.askinteger("Update Task", "Enter Task Number:")
        if index is not None:
            new_task_description = simpledialog.askstring("Update Task", "Enter New Task Description:")
            if new_task_description and self.todo_list.update_task(index - 1, new_task_description.strip()):
                messagebox.showinfo("Success", "Task updated successfully.")
            else:
                messagebox.showerror("Error", "Invalid task number or description.")

    def delete_task(self):
        """Delete a task via a dialog box."""
        index = simpledialog.askinteger("Delete Task", "Enter Task Number:")
        if index is not None and self.todo_list.delete_task(index - 1):
            messagebox.showinfo("Success", "Task deleted successfully.")
        else:
            messagebox.showerror("Error", "Invalid task number.")

if __name__ == "__main__":
    # The following lines check if this script is the 'main' program and runs the app if it is.
    root = tk.Tk()
    app = App(root)
    root.mainloop()
