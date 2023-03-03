#Dallas Lawson
#Final Project

#Feb. 28, 2023 progress
#I got the code from the following link: https://likegeeks.com/python-gui-examples-tkinter-tutorial/
#Hopefully, this will help me with the GUI.

from tkinter import *
from tkinter import END
from tkinter import messagebox
import os

window = Tk()
window.title("GameStop")
window.geometry('770x480') #This is the size of the window.
lbl = Label(window, text="GameStop's Inventory", font=("Times New Roman", 20))
lbl.grid(column=0, row=0)
btn = Button(window, text="Now I Am Become Death, The Destroyer Of Worlds.", command=lambda: window.destroy()) #This is to destroy the window.
btn.grid(column=1, row=0)

#Mar. 1, 2023 progress update 2
#I got the code from the following link: https://www.youtube.com/watch?v=pEP9Ma5UGPU
#It's not 100% exact from the video, but I would still have to mention it.

t1 = Text(window, height=26, width=95)
t1.grid(column=0, row=1, columnspan=2, pady=15)
font1 = ("Times New Roman", 15)
t1.insert(END, """This is the inventory of the location:
SpongeBob SquarePants: Battle for Bikini Bottom Rehydrated - 10 (Sell: $19.99; Buy: $10.00)
Spongebob Squarepants: Cosmic Shake - 12 (Sell: $19.99; Buy: $10.00)
Grand Theft Auto V (PS3) - 7 (Sell: $19.99; Buy: $10.00)
Grand Theft Auto V (PS4) - 55 (Sell: $29.99; Buy: $17.50)
Grand Theft Auto V (PS5) - 22 (Sell: $24.99; Buy: $15.00)
Grand Theft Auto V (Xbox 360) - 5 (Sell: $19.99; Buy: $10.00)
Grand Theft Auto V (Xbox One) - 30 (Sell: $29.99; Buy: $17.50)
Grand Theft Auto V (Xbox Series S/X) - 19 (Sell: $24.99; Buy: $15.00)
MSI Pulse GL66 Laptop - 2 (Sell: $1199.99; Buy: $800.00)
Nintendo Switch - 11 (Sell: $349.99; Buy: $200.00)
Nintendo Switch Lite - 8 (Sell: $299.99; Buy: $175.00)
Nintendo Switch OLED - 2 (Sell: $399.99; Buy: $300.00)
PlayStation 3 System (Pre-Owned) - 2 (Sell: $99.99; Buy: $50.00)
PlayStation 4 System (Pre-Owned) - 50 (Sell: $249.99; Buy: $185.00)
PlayStation 5 System (New) - 9 (Sell: $449.99; Buy: N/A)
Xbox 360 System (Pre-Owned) - 3 (Sell: $99.99; Buy: $50.00)
Xbox One System (Pre-Owned) - 44 (Sell: $199.99; Buy: $100.00)
Xbox Series X/S System (New) - 11 (Sell: $449.99; Buy: N/A)""")

#Mar. 1, 2023 progress update 1
#I got the code from the following link: https://community.spiceworks.com/topic/2234574-how-can-i-open-another-window-using-tkinter
#I decided to have two windows, one for the inventory and one for scanning the games, payment, etc.

def check_pass():
	username = user_entry.get()
	password = pass_entry.get()
	if username == 'user' and password == 'pass':
		root.destroy()
		main = Tk(className = 'GameStop')
		width = main.winfo_screenwidth() / 2
		height = 480
		main.geometry('%dx%d' % (width, height))
		main.mainloop()
	else:
		messagebox.showwarning('Incorrect Information', 'The username or password you entered is incorrect.')
root = Tk(className = 'Login')
Label(root, text='Username:').grid(row=0)
Label(root, text='Password:').grid(row=1)
user_entry = Entry(root)
pass_entry = Entry(root)
user_entry.grid(row=0, column=1)
pass_entry.grid(row=1, column=1)
button = Button(root, text = 'Enter', command=check_pass)
button.grid(row=2, column=0, columnspan=2)
root.mainloop()

window.mainloop()