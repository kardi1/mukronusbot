import pyautogui
import time
from Events import Events

class GameActions:
    resetLevel = 350
    def __init__(self) -> None:
        self.events = Events()

    def mover (self, x, y, t):
        pyautogui.moveTo(x, y)
        pyautogui.mouseDown()
        time.sleep(t)
        pyautogui.mouseUp()
        time.sleep(0.5)

    def reparar (self):
        self.events.rodarComando('/move atlans')
        time.sleep(1)
        self.events.clicarTecla('v')
        pyautogui.moveTo(1470,850)
        self.events.clicarMouse()
        pyautogui.moveTo(1375,320)
        self.events.clicarMouse()
        self.events.clicarMouse()
        self.events.clicarTecla('v')
        pyautogui.moveTo(950,400)

    def getLevel(self):
        level = self.events.readScreen(1431,197,1454,211)
        # fix problematic level
        if (level.isdigit() and int(level) == 238):
            level = '28'
        if (level.isdigit() and int(level) == 238):
            level = '40'
        return level
    
    def getCoordX(self):
        return self.events.readScreen(195,950,245,975)
    
    def getCoordY(self):
        return self.events.readScreen(255,950,305,975)
    
    def colocarDesfarce (self):
        time.sleep(1)
        self.events.clicarTecla('v')
        pyautogui.moveTo(1705,750)
        self.events.clicarMouse()
        pyautogui.moveTo(1450,390)
        self.events.clicarMouse()
        self.events.clicarTecla('v')

    def tirarDesfarce (self):
        time.sleep(1)
        self.events.clicarTecla('v')
        pyautogui.moveTo(1450,390)
        self.events.clicarMouse()
        pyautogui.moveTo(1705,750)
        self.events.clicarMouse()
        self.events.clicarTecla('v')

    def bater (self, levelGoal):
        startTime = time.time()
        pyautogui.moveTo(735,500)
        self.events.clicarTecla('c')
        time.sleep(10)
        levelText = self.getLevel()
        oldLevel = levelText
        i = 1
        y = 1
        stuck = 1
        while i <= 2 and y <= 100 and stuck < 10:
            if (levelText.isdigit()):
                if (int(levelText) <= int(self.resetLevel) and int(levelText) < int(levelGoal)):
                    if (oldLevel == levelText and int(levelText) >= 32):
                        stuck += 1
                    else:
                        stuck = 1
                        oldLevel = levelText
                    time.sleep(3)
                    i = 1
            else:
                time.sleep(3)
                i = 1
            time.sleep(1)
            levelText = self.getLevel()
            i += 1
            y += 1
        self.events.escreverLog('lv: ' + levelText + ', t: ' + str(y))
        endTime = time.time()
        tempoSpot = 'spot dur.: ' + time.strftime("%Mm %Ss", time.gmtime(endTime - startTime))
        self.events.escreverLog(tempoSpot)
        self.events.clicarTecla('c')
        return [levelText, y]
    
    def iniciaLorencia (self):
        coordX = self.getCoordX()
        coordY = self.getCoordY()
        coordText = str(coordX) + ', ' + str(coordY)
        self.events.escreverLog('coord: ' + coordText)
        #if (coordX.isdigit() and coordY.isdigit()):
        #    if (int(coordX) <= 136 and int(coordY) <= 123):
        #        self.mover(1235, 495, 2)
        #    if (int(coordX) >= 144 and int(coordY) >= 128):
        #        self.mover(510, 435, 2)
        if (coordX.isdigit() and coordY.isdigit()):
            coordX = int(coordX)
            coordY = int(coordY)
            if (coordX <= 142):
                segundos = (coordY - (coordX - 15))/5
                if (segundos > 0):
                    self.mover(720, 610, segundos)
            else:
                segundos = ((coordX - 15) - coordY)/5
                if (segundos > 0):
                    self.mover(735, 300, segundos)
        coordX = self.getCoordX()
        coordY = self.getCoordY()
        coordText = str(coordX) + ', ' + str(coordY)
        self.events.escreverLog('init: ' + coordText)
        
    def goToSetStartArea (self):
        pyautogui.moveTo(415, 440)
        pyautogui.mouseDown()
        layer = 0
        while (layer <= 5):
            coordX = self.getCoordX()
            coordY = self.getCoordY()
            #print(str(coordX) + ', ' + str(coordY))
            if (coordX.isdigit() and coordY.isdigit()):
                if (int(coordX) <= 133 and int(coordY) <= 116):
                    pyautogui.mouseUp()
                    coordText = str(coordX) + ', ' + str(coordY)
                    self.events.escreverLog('cheguei: ' + coordText)
                    time.sleep(10)
                    return
            time.sleep(1)
            layer += 1
            print('indo...')
        pyautogui.mouseUp()

    def distribuiPontos (self, i):
        #points = i * 100
        #if (points > 32700):
        #    points = 32700
        self.events.rodarComando('/zen')
        #self.events.rodarComando('/a ' + str(points))
        #self.events.rodarComando('/e ' + str(points))
        self.events.rodarComando('/e 32737')
        self.events.rodarComando('/a 32741')
        self.events.rodarComando('/v 32741')
        self.events.rodarComando('/f 32741')

    def checkPontoInicial (self):
        layer = 0
        while (layer <= 5):
            coordX = self.getCoordX()
            coordY = self.getCoordY()
            #print(str(coordX) + ', ' + str(coordY))
            if (coordX.isdigit() and coordY.isdigit()):
                if (int(coordX) == 114 and int(coordY) == 108):
                    return
            time.sleep(1)
            layer += 1

    def resetar (self, i):
        #self.events.rodarComando('/move davias')
        #self.colocarDesfarce()
        self.events.rodarComando('/resetar')
        time.sleep(2)
        self.iniciaLorencia()
        pyautogui.moveTo(415, 440)
        #pyautogui.moveTo(990, 175)
        pyautogui.mouseDown()
        self.distribuiPontos(i)
        self.checkPontoInicial()
        pyautogui.mouseUp()