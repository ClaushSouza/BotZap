#1. Primeiro vamos importar a bibliotecas

import pywhatkit
import keyboard
import time
from datetime import datetime
#2. Definir para quais contatos iremos enviar as msgs
contatos = ['+5511953400149', '+5511996211329']

# 3. vamos por um intervalo de envio de msgs

while len(contatos) >=1:
    #enviar mensagens
    pywhatkit.sendwhatmsg(contatos[0], 'Sei lá!', datetime.now(
    ).hour, datetime.now().minute + 2)
    del contatos[0]
    time.sleep(10)
    keyboard.press_and_release('crtl + w')