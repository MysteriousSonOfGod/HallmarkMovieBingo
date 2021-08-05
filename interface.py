import tkinter as tk
import importlib
from tkinter import filedialog, Text
import os

hallmark = importlib.import_module('hallmark')
root = tk.Tk()


def run_board_builder():
    hallmark.run(5)


canvas = tk.Canvas(root, height=700, width=900, bg="#263d42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

confirm = tk.Button(frame, text="OK", padx=10, pady=5, fg="white", bg="#263d42", command=run_board_builder())
confirm.pack()

root.mainloop()
