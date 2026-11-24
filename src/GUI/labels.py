from tkinter import *

# combines each label into a singular widget for ease of placement
def info_label(root):
    frame = Frame(root, width=100, height=120)
    frame.propagate(False)
    x = x_label(frame)
    y = y_label(frame)
    scale = scale_label(frame)
    iter = iterations_label(frame)
    x.place(relx=0.0, rely=0.0)
    y.place(relx=0.0, rely=0.0, y=30)
    scale.place(relx=0.0, rely=0.0, y=60)
    iter.place(relx=0.0, rely=0.0, y=90)
    return frame

# creates each label 
# OPTIMIZE: possible in a single function i think
def x_label(root):
    return Label(root, text="middle x: ")

def y_label(root):
    return Label(root, text="middle y: ")

def iterations_label(root):
    return Label(root, text="max iterations: ")

def scale_label(root):
    return Label(root, text="scale: ")