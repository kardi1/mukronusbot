import pyautogui
import time
import pytesseract
import re
from datetime import date
from PIL import ImageGrab
import EnvVariables
from os import path

class Events:
    def __init__(self) -> None:
        pytesseract.pytesseract.tesseract_cmd = EnvVariables.tesseractCmd

    def rodarComando (self, comando):
        #pyautogui.moveTo(455,940)
        pyautogui.press('enter')
        time.sleep(0.3)
        pyautogui.write(comando)
        time.sleep(0.3)
        pyautogui.press('enter')
        time.sleep(0.7)

    def clicarTecla (self, tecla):
        time.sleep(0.3)
        pyautogui.keyDown(tecla)
        time.sleep(0.3)
        pyautogui.keyUp(tecla)
        time.sleep(0.3)

    def clicarMouse (self):
        time.sleep(0.3)
        pyautogui.mouseDown()
        time.sleep(0.3)
        pyautogui.mouseUp()
        time.sleep(0.3)

    def readScreen(self, left, top, right, bottom):
        text = ''
        try:
            pic = ImageGrab.grab(bbox=(left,top,right,bottom))
            text = pytesseract.image_to_string(pic)
            text = text.strip()
            text = re.sub(r'[^0-9]', '', text)
        except FileNotFoundError as error:
            print(error)
        except:
            print('Read Screen Error')
        return text
    
    def escreverLog (self, message):
        print(message)
        startDay = int(date.today().strftime("%d"))
        try:
            f = open("logs/console" + str(startDay) + ".txt", "a")
            f.write(message + "\n")
            f.close()
        except:
            print('Algo deu errado ao escrever no arquivo!')
            
    def getResetsDoDia(self):
        startDay = int(date.today().strftime("%d"))
        filePath = "logs/resetsDoDia" + str(startDay) + ".txt"
        currentReset = 1
        try:
            if path.exists(filePath):
                f = open(filePath, "r")
                currentReset = f.read()
                f.close()
        except:
            print('Algo deu errado ao ler o arquivo!')
        return int(currentReset)
    
    def setResetsDoDia(self, resets):
        startDay = int(date.today().strftime("%d"))
        filePath = "logs/resetsDoDia" + str(startDay) + ".txt"
        try:
            f = open(filePath, "w")
            f.write(str(resets))
            f.close()
        except:
            print('Algo deu errado ao escrever no arquivo!')