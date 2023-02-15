import os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()

def run_file():
    file_path = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select file", filetypes=[("Python files", "*.py")])
    if file_path:
        os.system(f"python {file_path}")

run_button = tk.Button(root, text="Run file", command=run_file)
run_button.pack()

root.mainloop()
