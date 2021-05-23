from tkinter import *


ventana = Tk()

def Sumar():
    n1 = TxtNum1.get()
    n2 = TxtNum2.get()
    r = float(n1) + float(n2)
    TxtNum3.delete(0, END)
    TxtNum3.insert(0,r)

def Restar():
    n1 = TxtNum1.get()
    n2 = TxtNum2.get()
    r = float(n1) - float(n2)
    TxtNum3.delete(0, END)
    TxtNum3.insert(0, r)

def Multiplicar():
    n1 = TxtNum1.get()
    n2 = TxtNum2.get()
    r = float(n1) * float(n2)
    TxtNum3.delete(0, END)
    TxtNum3.insert(0, r)

def dividir():
    n1 = TxtNum1.get()
    n2 = TxtNum2.get()
    r = float(n1) // float(n2)
    TxtNum3.delete(0, END)
    TxtNum3.insert(0, r)

ventana.config(bg="blue")
ventana.geometry("570x450")
ventana.resizable(False,False)

Lbl1 = Label(ventana, text = "Primer numero", bg = "yellow", fg="red", font=("Helveita",16))
Lbl1.place(x=10, y=10, width=150, height=40)
TxtNum1 = Entry(ventana, bg="pink", bd=6, font=("helveita",17))
TxtNum1.place(x=10, y=70 ,width=150 ,height=40)

lbl2 = Label(ventana, text = "Segundo numero", bg="yellow", fg="red", font=("Helveita",16))
lbl2.place(x=195, y=10, width=170, height=40)
TxtNum2 = Entry(ventana, bg="pink", bd=6, font=("Helveita",17))
TxtNum2.place(x=193, y=70 ,width=170 ,height=40)

lbl3 = Label(ventana, text = "Resultado", bg="yellow", fg="red", font=("Helveita",16))
lbl3.place(x=10, y=150, width=130, height=40)
TxtNum3 = Entry(ventana, bg="pink", font=("Helveita",15),)
TxtNum3.place(x=10,y=200,width=130,height=40)

lbl3 = Label(ventana, text = "Botones de operaciones", bg="orange",font=("Helveita",16))
lbl3.place(x=190, y=200, width=235, height=40)

#aqui van los botones para realizar una operacion

btn1Suma = Button(ventana, text = "Suma", bg = "lightblue", bd=6, command=Sumar,font="Helveita,16")
btn1Suma.place(x=191,y=260, width=100,height=60)

btn2Resta = Button(ventana, text = "Resta", bg = "violet", bd=6, command=Restar,font=("Helveita",16))
btn2Resta.place(x=295,y=260,width=100,height=60)


btn3Multiplicacion = Button(ventana, text = "Multiplicacion", bg = "green", bd=6, command=Multiplicar,font=("Helveita",16))
btn3Multiplicacion.place(x=400,y=260,width=136,height=60)


btn4divicion = Button(ventana, text = "Divicion", bg = "greenyellow", bd=6, command=dividir,font=("Helveita",16))
btn4divicion.place(x=190,y=330,width=136,height=60)

ventana.mainloop()