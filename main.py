import time
from datetime import date
from Maps import Maps
from GameActions import GameActions
from Telegram import Telegram
from Events import Events
from QualityControl import QualityControl

#import pyautogui
#print(pyautogui.position())

nResets = input("Quantos resets você gostaria de dar? [padrão é 250] ")
time.sleep(3)
if (not nResets):
    nResets = 250

gameActions = GameActions()
maps = Maps()
telegram = Telegram()
events = Events()
qualityControl = QualityControl()

qualityControl.iniciandoBot()
startDay = int(date.today().strftime("%d"))
reportString = "/////////////////////////////////////////////////\n"
i = events.getResetsDoDia()
currentNReset = i
loops = 0
while i <= int(nResets):
    # reseta o dia para saber a quantidade de resets diário
    currentDay = int(date.today().strftime("%d"))
    if (startDay != currentDay):
        startDay = currentDay
        #i = 1
    startTime = time.time()
    events.escreverLog('####################')
    events.escreverLog(str(i) + ' resets')
    gameActions.resetar(i, loops)
    loops += 1
    maps.lorencia()
    maps.stadium()
    if (i % 3 == 0):
        gameActions.reparar()
    maps.icarus1()
    report = maps.icarus()
    #report = maps.kalima()
    checkReset = qualityControl.checkReset(report, i, startTime, reportString, nResets)
    reportString = checkReset[0]  
    currentNReset = i  
    i = checkReset[1]
events.rodarComando('/move davias')
reportString += "Bot finalizado!!! Número de resets: " + str(currentNReset) + "\n"
while (not telegram.sendMessage(reportString)):
    time.sleep(5)
