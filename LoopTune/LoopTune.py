import datetime
import time
from shutil import copyfile
from playsound import playsound
from tkinter import *
import tkinter as tk

#Cria a janela principal
win = Tk()
win.title("LoopTune")
win.geometry("350x233")
win.resizable(width=False, height=False)

#Coloca a imagem no plano de fundo
bg = PhotoImage(file = "lasalle1.png")
label1 = Label( win, image = bg)
label1.place(x = 0, y = 0)

#Caixa de entrada para as horas
h = Entry(win)
h.place(x = 15, y = 140, width=20)

#Caixa de entrada para os minutos
m = Entry(win,width=5)
m.place(x = 45, y = 140, width=20)

#Exibe informações do progama
eta =Label(win, text="")
eta.place(x = 15, y = 70, width=142)

#Cria a tela de configurações

def config():
    config = tk.Toplevel()
    config.title("Configurações")
    config.geometry("300x180")
    config.resizable(width=False, height=False)
    sound = Label(config, text="Insira o caminho do arquivo MP3")
    sound.place(x =65 , y = 30, width=200)
    s = Entry(config)
    s.insert(0,"./audio/AUDIO.MP3")
    s.place(x = 85, y = 70, width=142)
    def updateSound():#FUTURAMENTE ADD 2 PARAMETROS, ARQUIVO E DESTINO
        eta["text"] = "Audio atualizado"
        copyfile(path,"./AUDIO.MP3")
        config.destroy()
    button = Button(config, text="Salvar",command=updateSound)
    button.place(x =120 , y = 100, width=40)
    path = str(s.get())

#Cria o menu
menu=Menu(win)
win.config(menu=menu)

#Cria um item de menu
configMenu = Menu(menu)
menu.add_cascade(label="configurações", menu=configMenu)
configMenu.add_command(label="Caminho", command=config)
configMenu.add_command(label="Sair", command=win.destroy)

def reproduzir(mensagem):
    eta["text"] = "Reproduzindo"
    playsound(mensagem,False)
    
#def parar():
#    eta["text"] = "Interrompido"
#    playsound('./silence.mp3',False)

def loop():
    agora = datetime.datetime.now().time()
    agora_em_segundos =int((agora.hour*60*60)+(agora.minute*60) + agora.second)
    hi = int(h.get())
    mi = int(m.get())
    hora_em_segundos = ((hi*60*60) + (mi*60))
    hora = datetime.time(hi, mi)
    if agora >= hora:
        if hora_em_segundos - agora_em_segundos ==0:
            reproduzir('./AUDIO.mp3')
    else:
        eta["text"] = f"Faltam {hora_em_segundos - agora_em_segundos} segundos"
        win.after(1000,loop)

#Cria os botões
botao = Button(win, text="Iniciar",command=loop)
#config = Button(win, text="Configurações",command=config)
botao.place(x =120 , y = 200, width=40)
#config.place(x =265 , y = 0, width=80)
#parar = Button(win, text="Parar",command=parar)
#parar.place(x =180 , y = 200, width=40)

win.mainloop()
