#Dallas Lawson
#Feb. 28, 2023
#Final Project

#Feb. 28, 2023 progress update
#I did get the code from the following link: https://likegeeks.com/python-gui-examples-tkinter-tutorial/
#Hopefully, this will help me with the GUI.

from tkinter import *

window = Tk()
window.title("GameStop")
window.geometry('1080x720') #This is the size of the window.
lbl = Label(window, text="Welcome to GameStop", font=("Times New Roman", 15))
lbl.grid(column=0, row=0)
btn = Button(window, text="Now I Am Become Death, The Destroyer Of Worlds.", command=lambda: window.destroy()) #This is to destroy the window.
btn.grid(column=1, row=0)
window.mainloop()