from tkinter import *

def info_entry(root):
    frame = Frame(root, width=200, height=120)
    frame.propagate(False)
    x = x_entry(frame)
    y = y_entry(frame)
    scale = scale_entry(frame)
    iter = iterations_entry(frame)
    x.insert(0, "0")
    y.insert(0, "0")
    scale.insert(0, "0.01")
    iter.insert(0, "100")
    x.place(relx=0.0, rely=0.0)
    y.place(relx=0.0, rely=0.0, y=30)
    scale.place(relx=0.0, rely=0.0, y=60)
    iter.place(relx=0.0, rely=0.0, y=90)
    
    def get_values():
        return {
            "x": float(x.get()),
            "y": float(y.get()),
            "scale": float(scale.get()),
            "iter": int(iter.get())
        }
    
    return frame, get_values


def x_entry(root):
    return Entry(root, width=20)

def y_entry(root):
    return Entry(root, width=20)

def iterations_entry(root):
    return Entry(root, width=20)

def scale_entry(root):
    return Entry(root, width=20)