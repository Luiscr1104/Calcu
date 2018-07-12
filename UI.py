# -*- coding: utf-8 -*-
from Tkinter import *
from Calculadora import *
ventana = Tk()
#ventana.geometry("330x450")
ventana.title("Calculadora")
ventana.iconbitmap('Calculator.ico')

frame = Frame()
frame.config(bg="whitesmoke")
frame.grid(column=0, row=0, padx=(50, 50), pady=(50, 50))
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

valor = ""
pantalla = Entry(frame, width=25, textvariable=valor)
pantalla.grid(column=1, row=1, columnspan=5)

btn_0 = Button(frame, text="0", width=3)
btn_0.grid(row=5, column=1)

btn_coma = Button(frame, text=",", width=3)
btn_coma.grid(row=5, column=2)

btn_porcentaje = Button(frame, text="%", width=3)
btn_porcentaje.grid(row=5, column=3)

btn_sum = Button(frame, text="+", width=3)
btn_sum.grid(row=5, column=4)

btn_1 = Button(frame, text="1", width=3)
btn_1.grid(row=4, column=1)

btn_2 = Button(frame, text="2", width=3)
btn_2.grid(row=4, column=2)

btn_3 = Button(frame, text="3", width=3)
btn_3.grid(row=4, column=3)

btn_resta = Button(frame, text="-", width=3)
btn_resta.grid(row=4, column=4)

btn_4 = Button(frame, text="4", width=3)
btn_4.grid(row=3, column=1)

btn_5 = Button(frame, text="5", width=3)
btn_5.grid(row=3, column=2)

btn_6 = Button(frame, text="6", width=3)
btn_6.grid(row=3, column=3)

btn_multi = Button(frame, text="x", width=3)
btn_multi.grid(row=3, column=4)

btn_7 = Button(frame, text="7", width=3)
btn_7.grid(row=2, column=1)

btn_8 = Button(frame, text="8", width=3)
btn_8.grid(row=2, column=2)

btn_9 = Button(frame, text="9", width=3)
btn_9.grid(row=2, column=3)

btn_div = Button(frame, text="÷", width=3)
btn_div.grid(row=2, column=4)

btn_hexa_binario = Button(ventana, text="Convertir a Binario", width=15, command= lambda:hexa_binario())
btn_hexa_binario.grid(row=8, column=2)

ventana.mainloop()