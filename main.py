from tkinter import *
from src.GUI import *

# set global variables
width = 540
height = 720

# create and set screen and root variable
root = Tk()
root.title("Mandolbrot app")
root.geometry(f"{width}x{height}")

def main():    
    # create assignment and place the label text in the window
    label = info_label(root)
    label.place(x=10, y=10, anchor="nw")
    
    # create input assignment and a function to retrieve the values from the entry boxes, and place the entry boxes in the window
    input, get_values = info_entry(root)
    input.place(x=130, y=10, anchor="nw")
    
    run_button = run_widget(root, lambda: print_values(get_values()))
    run_button.place(x=10, y=125)
    
    canvas = Canvas(root, bg="black", height=520, width=510)    
    canvas.place(x=10, y=155, anchor="nw")
    
    exit_button = exit_widget(root)
    exit_button.place(relx=1.0, rely=1.0, x=-10, y=-10, anchor="se")
    mainloop()
    
def print_values(get_values):
    values = get_values
    print(values)

if __name__ == "__main__":
    main()
    
