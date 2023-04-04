import datetime
import time
from playsound import playsound

def reproduzir(mensagem):
    playsound(mensagem)

while True:
    agora = datetime.datetime.now().time()
    sete_55 = datetime.time(7, 55)
    if agora >= sete_55:
        reproduzir('C:/Users/lasalle/Desktop/AUDIO PASTORAL 16-03-2023-B-.mp3')
        break
    #time.sleep(60)
