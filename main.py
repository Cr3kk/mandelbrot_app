from tkinter import *
from src.GUI import *
from src.Math import *

# set global variables
width = 540
height = 720

# create and set screen and root variable
root = Tk()
root.title("Mandolbrot app")
root.geometry(f"{width}x{height}")

def main():    
    # create assignment and place the label text in the window
    labels = info_label(root)
    labels.place(x=10, y=10, anchor="nw")
    
    # create input assignment and a function to retrieve the values from the entry boxes, and place the entry boxes in the window
    entry_fields, get_values = info_entry(root)
    entry_fields.place(x=130, y=10, anchor="nw")

    # draws the canvas on which the mandelbrot funciton is being drawn
    canvas = Canvas(root, height=500, width=500)    
    canvas.place(x=15, y=165, anchor="nw")

    # creates an image to put onto the canvas at runtime, used at every button press and at runtime once
    img = PhotoImage(width=500, height=500)
    canvas.create_image(0, 0, image=img, anchor="nw")
    canvas.image = img 

    def run_command():
        x, y, scale, max_iter = get_values()
        
        mandolbrot_set = calculate_mandolbrot_set(x, y, scale, max_iter)
        img.configure(data=count_to_image(mandolbrot_set, max_iter), format="PPM") # sets the image using the converter function to get white and black
        
        
    # create the run button
    run_button = run_widget(root, run_command)
    run_button.place(x=10, y=125)

    run_command()
    
    #c reates exit button to close the programa
    exit_button = exit_widget(root)
    exit_button.place(relx=1.0, rely=1.0, x=-10, y=-10, anchor="se")
    mainloop()

if __name__ == "__main__":
    main()
    
