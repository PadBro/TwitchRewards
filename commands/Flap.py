import time
import pyautogui

def flap():
  time.sleep(1)
  pyautogui.mouseDown(button='right')
  time.sleep(1)
  pyautogui.mouseUp(button='right')
  return
  
