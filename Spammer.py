import pyautogui as pg
import time
import webbrowser as web
phone_no="+523333333333"
parsedMessage=" "
web.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+parsedMessage)
time.sleep(8)
for i in range(150):
    pg.write('We')
    pg.press('enter')
    print('Mensaje #'+str(i+1)+' enviado')
    pass
pg.alert('Bomba de mensajes finalizada')
