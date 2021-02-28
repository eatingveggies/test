from tkinter import *

window = Tk()

window.title("Nathan's Button")
window.iconbitmap('med.ico')

# making the object
b1 = Button(text = "Click Me!")

# placing the object
b1.grid(row = 0, column = 0)

window.mainloop()