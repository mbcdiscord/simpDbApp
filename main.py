from func import main
import tkinter as tk
from tkinter import *

home = Tk()
home.title("Animals Database")
home.geometry("1000x500")
home.config(background="grey")


inputFromEntry = tk.IntVar()
mainFont = ("Comic Sans MS", 20, "bold")


welcomeText = tk.Label(
    home,
    text="Animals Database Enter a number to get the animal details!",
)
welcomeText.config(font=mainFont, fg="blue")
welcomeText.pack()

inputEntry = tk.Entry(home, font=mainFont, textvariable=inputFromEntry)
inputEntry.pack()

submitBtn = tk.Button(
    home, font=mainFont, text="Get details...", command=main(inputFromEntry)
)
submitBtn.pack()


home.mainloop()
