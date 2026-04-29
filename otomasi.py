import os
import pyautogui # type: ignore # pip install pyautogui
import subprocess
import time
from datetime import datetime

subprocess.Popen('notepad.exe') # open notepad
time.sleep(2) # wait for notepad to open
pyautogui.write('Your Mom is Gay', interval=0.1) # type the text with a delay between each character
pyautogui.press('enter')

img = pyautogui.screenshot() # take a screenshot
img.save(os.path.join(os.getcwd(), f'screenshot_{datetime.now().strftime("%Y%m%d_%H%M%S")}.png')) # save the screenshot with a timestamp in the filename

print('Screenshot taken and saved successfully.') # print a success message