from distutils.cmd import Command
import tkinter as Tk
from tkinter import *
from turtle import left

from Calculadora import vista_tkinter

mainT = Tk()
mainT.title("Digital MultiTool")
mainT.resizable(1,1)
mainT.geometry("1320x720")

Titulo = Label(mainT, text="Digital MultiTool Software", font=("Arial", 20))
Titulo.pack()

btn_calculadora = Button(mainT, height="3",text="Calculadora Basica con Fracciones", command=vista_tkinter)
btn_calculadora.place(x=50, y=250)

mainT.mainloop()