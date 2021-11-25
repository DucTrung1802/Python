import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo

root = tk.Tk()
root.title("Tkinter messagebox")
root.resizable(False, False)
root.geometry("300x150")

options = {'fill': 'both', 'padx': 10, 'pady': 10, 'ipadx': 5}

ttk.Button(
    root,
    text="Show an error message",
    command=lambda: showerror(
        title='Error',
        message="This is an error message.")
).pack(options)


ttk.Button(
    root,
    text="Show an warning message",
    command=lambda: showwarning(
        title='Error',
        message="This is an warning message.")
).pack(options)


ttk.Button(
    root,
    text="Show an info message",
    command=lambda: showinfo(
        title='Error',
        message="This is an info message.")
).pack(options)

root.mainloop()

