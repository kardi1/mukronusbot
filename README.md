# mubot
Bot para resetar sozinho no jogo Mu Online

Requisitos para executar este bot no windows:

- Baixar Visual Studio Code (executar como administrador)
- Baixar python (no Windows e no Visual Studio)
- Baixar pyautogui (pip install pyautogui)
- Baixar Pillow (pip install Pillow)
- Baixar pytesseract (https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i)
- Baixar requests (pip install requests)

Outras ferramentas:
- Baixar Git Bash (https://gitforwindows.org/)
- Gerar chaves ssh

Crie um arquivo chamado EnvVariables.py na raiz do projeto com 2 variáveis de ambiente:

```python
tesseractCmd = r'D:\<path-to-tesseract>\tesseract.exe'
screenshotSavingPath = r'D:\<path-to-logs>\logs\images\reset'
telegramToken = '<telegramToken>'
telegramChatId = '<telegramChatId>'
```