from tkinter import *

# combines each entry field into a single widget
def info_entry(root):
    frame = Frame(root, width=200, height=120)
    frame.propagate(False)
    x = x_entry(frame)
    y = y_entry(frame)
    scale = scale_entry(frame)
    iter = iterations_entry(frame)
    x.insert(0, "0") # sets a default value
    y.insert(0, "0") # same
    scale.insert(0, "0.01") # same
    iter.insert(0, "100") # same
    x.place(relx=0.0, rely=0.0)
    y.place(relx=0.0, rely=0.0, y=30)
    scale.place(relx=0.0, rely=0.0, y=60)
    iter.place(relx=0.0, rely=0.0, y=90)
    
    # creates a get function to combine the values from the entry fields into a single dict
    def get_values():
        return {
            "x": float(x.get()),
            "y": float(y.get()),
            "scale": float(scale.get()),
            "iter": int(iter.get())
        }
    
    return frame, get_values

# creates each entry field 
# OPTIMIZE: possible in a single function i think
def x_entry(root):
    return Entry(root, width=20)

def y_entry(root):
    return Entry(root, width=20)

def iterations_entry(root):
    return Entry(root, width=20)

def scale_entry(root):
    return Entry(root, width=20)