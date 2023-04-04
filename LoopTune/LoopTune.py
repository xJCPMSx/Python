import datetime
import time
from playsound import playsound
from tkinter import *
import tkinter as tk

def reproduzir(mensagem):
    playsound(mensagem,False)

win = Tk()
win.title("LoopTune")
win.geometry("230x150")
win.resizable(width=False, height=False)

bg= PhotoImage(file = "lasalle.png")
label1 = Label( win, image = bg)
label1.place(x = 0, y = 0)

hourtxt = Label(win, text="Insira a(s) hora(s) que deseja reproduzir")
hourtxt.grid(column=0, row=0)
h = Entry(win,width=5)
h.grid(column=0, row=1)

mintxt = Label(win, text="Insira o(s) minuto(s) que deseja reproduzir")
mintxt.grid(column=0, row=2)
m = Entry(win,width=5)
m.grid(column=0, row=3)

eta =Label(win, text="")
eta.grid(column=0, row=5)

t = 0
def loop():
    global t
    agora = datetime.datetime.now().time()
    hi = int(h.get())
    mi = int(m.get())
    hora = datetime.time(hi, mi)
    if agora >= hora:
        reproduzir('./AUDIO.mp3')
    else:
        eta["text"] = f"Se passaram {t} segundos"
        win.after(1000,loop)
        t+=1
            

botao = Button(win, text="Iniciar",command=loop) #,command=loop 
botao.grid(column=0, row=4)
       
win.mainloop()