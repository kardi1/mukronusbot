import time
from datetime import date
from Maps import Maps
from GameActions import GameActions
from Telegram import Telegram
from Events import Events
from QualityControl import QualityControl

nResets = input("Quantos resets você gostaria de dar? [padrão é 950] ")
time.sleep(3)
if (not nResets):
    nResets = 950

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
while i <= int(nResets):
    # reseta o dia para saber a quantidade de resets diário
    currentDay = int(date.today().strftime("%d"))
    if (startDay != currentDay):
        startDay = currentDay
        #i = 1
    startTime = time.time()
    events.escreverLog('####################')
    events.escreverLog(str(i) + ' resets')
    gameActions.resetar(i)
    maps.lorencia()
    report = qualityControl.resetStepTwo()
    if (i % 3 == 0):
        events.rodarComando('/move davias')
        gameActions.reparar()
    checkReset = qualityControl.checkReset(report, i, startTime, reportString, nResets)
    reportString = checkReset[0]  
    currentNReset = i  
    i = checkReset[1]
events.rodarComando('/move davias')
reportString += "Bot finalizado!!! Número de resets: " + str(currentNReset) + "\n"
while (not telegram.sendMessage(reportString)):
    time.sleep(5)
