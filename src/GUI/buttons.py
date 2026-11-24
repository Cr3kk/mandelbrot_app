from tkinter import *

def run_widget(root, command):
    return Button(root, text="GO", command=command)

def exit_widget(root):
    return Button(root, text="Exit", command=root.destroy)
    