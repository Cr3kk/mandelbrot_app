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
    
    values = {}
    mandol_set = []

    # draws the canvas on which the mandelbrot funciton is being drawn
    canvas = Canvas(root, height=500, width=500)    
    canvas.place(x=15, y=165, anchor="nw")

    img = PhotoImage(width=500, height=500)
    canvas.create_image(0, 0, image=img, anchor="nw")
    canvas.image = img 

    def draw_mandolbrot_set(mandol_set):
        rows = ["{" + " ".join(row) + "}" for row in mandol_set]
        img.put(" ".join(rows), to=(0, 0))

    def run_command():
        nonlocal values, mandol_set, canvas
        values = get_values()
        mandol_set = calculate_mandolbrot_set(
            values["x"], values["y"], values["scale"], values["iter"]
        )
        draw_mandolbrot_set(mandol_set)

    
    # create the run button. TEMP: using placehold function to extract values
    # NOTE to add more commands for when the button runs, add it to the run_widget, then add a new command to it in src.GUI.buttons.py and put it in the run_commands function as well.
    run_button = run_widget(root, run_command)
    run_button.place(x=10, y=125)

    run_command()
    
    #creates exit button to close the programa
    exit_button = exit_widget(root)
    exit_button.place(relx=1.0, rely=1.0, x=-10, y=-10, anchor="se")
    mainloop()

# NOTE semanctics used when creating real applications and enterprise software, kinda pointless but i thought it was fun
if __name__ == "__main__":
    main()
    
