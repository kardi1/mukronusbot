import time
from Events import Events
from GameActions import GameActions
from datetime import datetime
import pyautogui

class Maps:
    levelFirstSpot = 32
    levelSecondSpot = 170
    levelThirdSpot = 250

    def __init__(self) -> None:
        self.gameActions = GameActions()
        self.events = Events()

    def lorenciaNew (self):
        self.gameActions.mover(1435, 485, 4)
        self.gameActions.mover(950, 160, 6)
        self.gameActions.mover(600, 240, 6)
        pyautogui.moveTo(960, 465)
        time.sleep(2)
        self.gameActions.mover(1020, 195, 1)
        self.gameActions.mover(1145, 295, 1)
        self.gameActions.bater(self.levelFirstSpot)

    def lorencia (self):
        layer = 0
        while (layer <= 5):
            coordX = self.gameActions.getCoordX()
            coordY = self.gameActions.getCoordY()
            if (coordX.isdigit() and coordY.isdigit()):
                #currentHour = int(datetime.now().hour)
                if (int(coordX) == 149 and int(coordY) == 108):
                    #if (currentHour > 2 and currentHour < 8):
                    #    self.bufalos()
                    #else:
                    self.esqueleto()
                    return
                if (int(coordX) == 153 and int(coordY) == 118):
                    #if (currentHour > 2 and currentHour < 8):
                    #    self.aranhas()
                    #else:
                    self.gameActions.mover(700, 465, 3)
                    self.gameActions.mover(1120, 670, 5)
                    self.esqueleto()
                    return
            else:
                # vai para o ponto inicial de lorencia
                self.gameActions.mover(700, 465, 3)
                self.gameActions.mover(1120, 670, 5)
                self.esqueleto()
                return
            self.gameActions.mover(950, 650, 1)
            layer += 1

    def esqueleto (self):
        self.gameActions.mover(1080, 190, 10.5)
        self.gameActions.tirarDesfarce()
        self.gameActions.mover(1280, 320, 15)
        # limpa mobs para poder andar
        time.sleep(2)
        self.gameActions.mover(920,230, 1)
        self.gameActions.bater(self.levelFirstSpot)

    def aranhas (self):
        self.gameActions.mover(1350, 290, 2.3)
        self.gameActions.mover(1240, 640, 9)
        time.sleep(2)
        self.gameActions.mover(1350, 505, 4.2)
        time.sleep(2)
        self.gameActions.mover(1135, 680, 1.2)
        self.gameActions.bater(self.levelFirstSpot)

    def bufalos (self):
        self.gameActions.mover(1080, 190, 3.2)
        self.gameActions.mover(735, 270, 2.3)
        self.gameActions.mover(620, 660, 11.2)
        time.sleep(2)
        self.gameActions.mover(1125, 670, 3)
        self.gameActions.bater(self.levelFirstSpot)

    def stadium2 (self, level):
        self.events.rodarComando('/move stadium')
        self.gameActions.mover(675, 650, 4.8)
        return self.gameActions.bater(level)

    def davias2 (self, level):
        self.events.rodarComando('/move davias2')
        self.gameActions.mover(745, 290, 3.4)
        time.sleep(2)
        self.gameActions.mover(680, 595, 2.2)
        return self.gameActions.bater(level)

    def stadium (self, level):
        self.events.rodarComando('/move stadium')
        self.gameActions.mover(1200, 600, 4.2)
        # limpa mobs para poder andar
        time.sleep(2)
        self.gameActions.mover(1240, 600, 1.8)
        return self.gameActions.bater(level)

    def icarus (self):
        self.events.rodarComando('/move icarus2')
        self.gameActions.mover(1110, 285, 0.5)
        # limpa mobs para poder andar
        time.sleep(2)
        self.gameActions.mover(1110, 285, 1)
        return self.gameActions.bater(self.gameActions.resetLevel)
    
    def icarus1 (self):
        self.events.rodarComando('/move icarus1')
        time.sleep(2)
        self.gameActions.mover(1190, 360, 0.7)
        time.sleep(2)
        self.gameActions.mover(1190, 360, 0.7)
        time.sleep(2)
        self.gameActions.mover(1190, 360, 0.7)
        self.gameActions.bater(self.levelThirdSpot)

    def kalima (self):
        self.events.rodarComando('/kalima')
        self.gameActions.mover(730, 450, 1)
        # limpa mobs para poder andar
        time.sleep(2)
        self.gameActions.mover(730, 450, 1)
        return self.gameActions.bater(self.gameActions.resetLevel)