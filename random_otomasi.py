import os
import pyautogui # type: ignore # python -m pip install pyautogui
import subprocess
import time
from datetime import datetime

subprocess.Popen(r'C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\game\bin\win64\cs2.exe')
time.sleep(10) # Wait for the game to launch

subprocess.Popen('notepad.exe')
time.sleep(2) # Wait for Notepad to open

pyautogui.write("Your CS is now open, let's play together init", interval=0.05)
pyautogui.press('enter')