import requests
import EnvVariables

class Telegram:
    def sendMessage (self, message):
        try:
            TOKEN = EnvVariables.telegramToken
            chat_id = EnvVariables.telegramChatId
            #url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
            #requests.get(url).json()
            return True
        except:
            print('Telegram Send Message Error')
            return False
        