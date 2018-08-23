import pyautogui as py
import time as t
py.click(1249,13)
py.moveTo(20,20,1)
py.doubleClick(20,20,0.1)
t.sleep(2)
py.moveTo(533,353,1)
py.doubleClick(533,353,0.1)
t.sleep(2)
py.rightClick(600,419,0.10)
t.sleep(2)
py.click(656,346)
t.sleep(2)
py.hotkey('ctrl', 'z')