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
    
    values = {} # init an empty dictionairy for use later
    # function that takes the values currently in the entry fields and puts them into a dictionairy (See: src.GUI.entries.get_values for labeling) TEMP: maybe change to what we need for drawing the mandelbrot
    def extract_values():
        new_values = get_values()
        print(new_values)
    
    # create the run button. TEMP: using placehold function to extract values
    # NOTE to add more commands for when the button runs, add it to the run_widget, then add a new command to it in src.GUI.buttons.py and put it in the run_commands function as well.
    run_button = run_widget(root, extract_values)
    run_button.place(x=10, y=125)
    
    # draws the canvas on which the mandelbrot funciton is being drawn
    canvas = Canvas(root, bg="black", height=520, width=510)    
    canvas.place(x=10, y=155, anchor="nw")
    
    #creates exit button to close the programa
    exit_button = exit_widget(root)
    exit_button.place(relx=1.0, rely=1.0, x=-10, y=-10, anchor="se")
    mainloop()

# NOTE semanctics used when creating real applications and enterprise software, kinda pointless but i thought it was fun
if __name__ == "__main__":
    main()
    
