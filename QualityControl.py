import pyautogui
import time
from Events import Events
from GameActions import GameActions
from Maps import Maps
from Telegram import Telegram
import EnvVariables
from datetime import datetime
import random

class QualityControl:
    def __init__(self) -> None:
        self.events = Events()
        self.gameActions = GameActions()
        self.maps = Maps()
        self.telegram = Telegram()

    def controle (self, i):
        self.events.clicarTecla('esc')
        pyautogui.moveTo(980,330)
        self.events.clicarMouse()
        # wait to load character screen
        time.sleep(3)
        pyautogui.moveTo(670,625)
        self.events.clicarMouse()
        pyautogui.press('enter')
        # wait to enter game after selecting char
        time.sleep(3)
        self.events.rodarComando('/re off')
        self.events.rodarComando('/party off')
        self.events.clicarTecla('1')
        pyautogui.screenshot().save(EnvVariables.screenshotSavingPath + str(i) + 'controle.png')

    def geradorDeFrase(self):
        frases = ['sou vampiraum','holy','fui','amigo','boa noite','to soh upando','pra cima deles','vamo dale','tragico','ops','nao eh moleza','aaaah tim','eh complicado','to vazando, mals','eu digito lento','suave?','falou, valeu','soh pedir pt','to na missao', '']
        frase = random.choice(frases)
        self.events.rodarComando(frase)

    def resetStepTwo (self):
        #self.geradorDeFrase()
        self.maps.stadium(200)
        #self.geradorDeFrase()
        #report = self.maps.kalima()
        report = self.maps.icarus()
        #self.geradorDeFrase()
        return report
    
    def isMadrugada (self, esperando = True):
        while (esperando):
            currentHour = int(datetime.now().hour)
            if (currentHour < 1 or currentHour > 10):
                time.sleep(2)
                print('Esperando a hora de jogar...')
                self.events.clicarTecla('c')
                time.sleep(1)
                self.events.clicarTecla('c')
                time.sleep(300)
            else:
                esperando = False
                if (currentHour > 7):
                    return False
        return True

    def iniciandoBot (self):
        self.events.rodarComando('/re off')
        self.events.rodarComando('/party on')
        return
        self.events.clicarTecla('c')
        level = self.gameActions.getLevel()
        self.events.clicarTecla('c')
        if (level.isdigit()):
            if (int(level) < self.gameActions.resetLevel):
                if (int(level) >= 32):
                    return self.resetStepTwo()

    def checkReset (self, report, i, startTime, reportString, nResets):
        currentReset = i
        if (report[0] and report[0].isdigit()):
            if (int(report[0]) < self.gameActions.resetLevel):
                if (int(report[0]) >= 32):
                    pyautogui.screenshot().save(EnvVariables.screenshotSavingPath + str(currentReset) + '-1.png')
                    reportString += "reset " + str(currentReset) + " não deu boa!"
                    reportString += " lv: " + str(report[0]) + "\n"
                    report = self.resetStepTwo()
            if (report[0] and report[0].isdigit() and int(report[0]) >= self.gameActions.resetLevel):
                i += 1
                self.events.setResetsDoDia(i)
        else:
            if ((not report[0]) and (int(report[1]) == 51)):
                if (self.gameActions.getCoordX() and self.gameActions.getCoordY()):
                    pyautogui.screenshot().save(EnvVariables.screenshotSavingPath + str(currentReset) + '-2.png')
                    reportString += "Algo deu errado, tentando consertar..." + "\n"
                    self.controle(i)
                else:
                    reportString += "Desconectado do jogo, encerrando bot!" + "\n"
                    i = int(nResets) + 1
        endTime = time.time()
        resetTime = time.strftime("%Mm %Ss", time.gmtime(endTime - startTime))
        reportString += "r:" + str(currentReset) + ",t:" + resetTime+ "; "
        #reportString += ", lv: " + str(report[0]) + ", t: " + str(report[1]) + "\n"
        if (i % 30 == 0):
            if (self.telegram.sendMessage(reportString)):
                reportString = ''
        self.events.escreverLog('time: ' + resetTime)
        return [reportString, i]