import os
import pyautogui # type: ignore # pip install pyautogui
import subprocess
import time
from datetime import datetime

pyautogui.FAILSAFE = False # disable failsafe to prevent the program from crashing if the mouse is moved to the corner of the screen

subprocess.Popen('notepad.exe') # open notepad
time.sleep(2) # wait for notepad to open
pyautogui.write('Your Mom is Gay', interval=0.05) # type the text with a delay between each character
pyautogui.press('enter')
pyautogui.write('Just Messing Around, CIAO', interval=0.05)
pyautogui.press('enter')
pyautogui.write(f'Checking Time RN {datetime.now().strftime("%H:%M")}', interval=0.05)
pyautogui.press('enter')