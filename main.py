from tkinter import *
from src import *

root = Tk()
root.title("Mandolbrot app")

width = 540
height = 720

canvas = Canvas(root, bg="grey75", width=720, height=1080)

def main():
    
    canvas.bind()
    mainloop()

if __name__ == "__main__":
    main()
