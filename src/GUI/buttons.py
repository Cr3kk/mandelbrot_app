from tkinter import *

# creates the button for runnning the program. Update and add amount of commands here
def run_widget(root, command1):
    def run_commands():
        command1()
    return Button(root, text="GO", command=run_commands)

# creates the button to close the program
def exit_widget(root):
    return Button(root, text="Exit", command=root.destroy)
    