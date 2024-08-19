import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from PIL import Image, ImageTk, ImageDraw


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do App")
        self.root.geometry("800x600")

        # Add a radial gradient background
        self.create_radial_gradient_background()

        self.tasks = []

        # Header
        self.header_label = tk.Label(self.root, text="📝 To-Do List", font=("Helvetica", 24, "bold"), bg="#6a1b9a",
                                     fg="white")
        self.header_label.pack(pady=20)

        # Motivational Quote
        self.quote_label = tk.Label(self.root, text='"The future depends on what you do today." - Mahatma Gandhi',
                                    font=("Helvetica", 14, "italic"), bg="#6a1b9a", fg="white")
        self.quote_label.pack(pady=10)

        # Task list
        self.task_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, width=80, height=20, bg="white", fg="black",
                                       font=("Helvetica", 12))
        self.task_listbox.pack(pady=20)

        # Task Buttons
        self.add_button = tk.Button(self.root, text="➕ Add Task", command=self.add_task, bg="#4CAF50", fg="white",
                                    font=("Helvetica", 12))
        self.add_button.pack(side=tk.LEFT, padx=10)

        self.delete_button = tk.Button(self.root, text="🗑️ Delete Task", command=self.delete_task, bg="#F44336",
                                       fg="white", font=("Helvetica", 12))
        self.delete_button.pack(side=tk.LEFT, padx=10)

        self.complete_button = tk.Button(self.root, text="✅ Mark Complete", command=self.mark_complete, bg="#2196F3",
                                         fg="white", font=("Helvetica", 12))
        self.complete_button.pack(side=tk.LEFT, padx=10)

        self.change_button = tk.Button(self.root, text="✏️ Change Task", command=self.change_task, bg="#FFEB3B",
                                       fg="black", font=("Helvetica", 12))
        self.change_button.pack(side=tk.LEFT, padx=10)

    def create_radial_gradient_background(self):
        # Create a radial gradient background
        gradient_image = Image.new("RGB", (800, 600), "#ffffff")
        draw = ImageDraw.Draw(gradient_image)
        for i in range(0, 300, 10):
            draw.ellipse([(400 - i, 300 - i), (400 + i, 300 + i)], fill=(255 - i // 2, 100 + i // 2, 150 + i // 2))

        self.bg_image = ImageTk.PhotoImage(gradient_image)
        self.bg_label = tk.Label(self.root, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)

    def add_task(self):
        task = simpledialog.askstring("Add Task", "Enter task description:")
        if task:
            self.tasks.append(task)
            self.update_task_list()

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            del self.tasks[task_index]
            self.update_task_list()
        else:
            messagebox.showwarning("Delete Task", "No task selected.")

    def mark_complete(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            self.tasks[task_index] += " ✅"
            self.update_task_list()
        else:
            messagebox.showwarning("Mark Complete", "No task selected.")

    def change_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            new_task = simpledialog.askstring("Change Task", "Enter new task description:")
            if new_task:
                self.tasks[task_index] = new_task
                self.update_task_list()
        else:
            messagebox.showwarning("Change Task", "No task selected.")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
