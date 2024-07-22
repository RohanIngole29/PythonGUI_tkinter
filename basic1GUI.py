from tkinter import *

root = Tk()
root.title("Basic GUI Program")

c = Canvas(root, bg="gray")
c.create_text(200, 50, text="First GUI using tkinter", fill="black",font="bold")
c.pack(padx=10, pady=20)

root.mainloop()
