import time
from pynput.keyboard import Key, Controller

def ball_up():
  keyboard = Controller()
  key = Key.alt_l
  time.sleep(5)
  keyboard.press(key)
  time.sleep(5)
  keyboard.release(key)
  return
