# -*- coding: utf-8 -*-
from Tkinter import *
raiz= Tk()
raiz.title("Calculadora")
raiz.iconbitmap('Calculator.ico')
raiz.geometry("330x450")
teclado=Frame()
teclado.pack(fill='both', expand="True")
teclado.config(width="376", height="362")
teclado.config(bg="whitesmoke")

#cuadroTexto= Entry(miFrame)
#cuadroTexto.place(x=100, y=100)
boton1 = Button(teclado, text="1")
boton1.grid(row=3, column=1)

boton2 = Button(teclado,text="2")
boton2.grid(row=3, column=2)

boton2 = Button(teclado,text="3")
boton2.grid(row=3, column=3)

boton2 = Button(teclado,text="4")
boton2.grid(row=2, column=1)

boton2 = Button(teclado,text="5")
boton2.grid(row=2, column=2)

boton2 = Button(teclado,text="6")
boton2.grid(row=2, column=3)

boton2 = Button(teclado,text="7")
boton2.grid(row=1, column=1)

boton2 = Button(teclado,text="8")
boton2.grid(row=1, column=2)

#Boton para la suma
btnsuma = Button(text="Suma", width=5)
btnsuma.pack()

raiz.mainloop()