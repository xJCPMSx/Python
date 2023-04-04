import datetime
import time
from playsound import playsound
from tkinter import *
import tkinter as tk

def reproduzir(mensagem):
    playsound(mensagem,False)

win = Tk()
win.title("LoopTune")
win.geometry("350x233")
win.resizable(width=False, height=False)

bg= PhotoImage(file = "lasalle1.png")
label1 = Label( win, image = bg)
label1.place(x = 0, y = 0)

#hourtxt = Label(win, text="Insira a(s) hora(s) que deseja reproduzir")
#hourtxt.grid(column=0, row=0)
h = Entry(win)
h.place(x = 15, y = 140, width=20)

#mintxt = Label(win, text="Insira o(s) minuto(s) que deseja reproduzir")
#mintxt.grid(column=0, row=2)
m = Entry(win,width=5)
m.place(x = 45, y = 140, width=20)

eta =Label(win, text="")
eta.place(x = 15, y = 70, width=142)

def loop():
    agora = datetime.datetime.now().time()
    agora_em_segundos =int((agora.hour*60*60)+(agora.minute*60) + agora.second)
    hi = int(h.get())
    mi = int(m.get())
    hora_em_segundos = ((hi*60*60) + (mi*60))
    hora = datetime.time(hi, mi)
    if agora >= hora:
        eta["text"] = f"Faltam {hora_em_segundos - agora_em_segundos} segundos"
        if hora_em_segundos - agora_em_segundos ==0:
            reproduzir('./AUDIO.mp3')
    else:
        eta["text"] = f"Faltam {hora_em_segundos - agora_em_segundos} segundos"
        win.after(1000,loop)
            

botao = Button(win, text="Iniciar",command=loop) #,command=loop 
botao.place(x =120 , y = 200, width=40)
       
win.mainloop()