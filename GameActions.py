import pyautogui
import time
from Events import Events

class GameActions:
    resetLevel = 310
    def __init__(self) -> None:
        self.events = Events()

    def mover (self, x, y, t):
        pyautogui.moveTo(x, y)
        pyautogui.mouseDown()
        time.sleep(t)
        pyautogui.mouseUp()
        time.sleep(0.5)

    def reparar (self):
        time.sleep(1)
        self.events.clicarTecla('v')
        pyautogui.moveTo(1470,850)
        self.events.clicarMouse()
        pyautogui.moveTo(1375,320)
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
        while i <= 2 and y <= 50 and stuck < 5:
            if (levelText.isdigit()):
                if (int(levelText) <= int(self.resetLevel) and int(levelText) < int(levelGoal)):
                    if (oldLevel == levelText):
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

    def resetar (self, i):
        self.events.rodarComando('/resetar')
        time.sleep(2)
        coordX = self.getCoordX()
        coordY = self.getCoordY()
        coordText = str(coordX) + ', ' + str(coordY)
        self.events.escreverLog('coord: ' + coordText)
        if (coordX.isdigit() and coordY.isdigit()):
            if (int(coordX) <= 136 and int(coordY) <= 123):
                self.mover(1235, 495, 1)
            if (int(coordX) >= 144 and int(coordY) >= 128):
                self.mover(510, 435, 1)
        pyautogui.moveTo(950, 650)
        pyautogui.mouseDown()
        points = i * 100
        if (points > 32700):
            points = 32700
        self.events.rodarComando('/zen')
        self.events.rodarComando('/a ' + str(points))
        self.events.rodarComando('/e ' + str(points))
        #self.events.rodarComando('/e 32737')
        #self.events.rodarComando('/a 32741')
        #self.events.rodarComando('/v 32741')
        #self.events.rodarComando('/f 32741')
        pyautogui.mouseUp()