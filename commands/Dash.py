import time
from pynput.keyboard import Key, Controller

def dash():
  keyboard = Controller()
  key = Key.ctrl_l
  time.sleep(1)
  keyboard.press(key)
  time.sleep(1)
  keyboard.release(key)
  return
