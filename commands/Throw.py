import time
import pyautogui

def throw():
  time.sleep(5)
  pyautogui.mouseDown()
  time.sleep(1)
  pyautogui.mouseUp()
  return
  
