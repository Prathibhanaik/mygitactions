import tkinter as tk

def button_click():
    label.config(text="Button clicked")

root = tk.Tk()
root.title("GitHub Actions GUI")

label = tk.Label(root, text="Welcome to GitHub Actions")
label.pack(pady=10)

button = tk.Button(root, text="Click me", command=button_click)
button.pack(pady=10)

root.mainloop()
