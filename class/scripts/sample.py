import pyautogui
import time
import os

os.system("mspaint")
time.sleep(3)

pyautogui.moveTo(200, 200)

pyautogui.dragTo(400, 400, duration=1)
time.sleep(1)

for i in range(5):
    pyautogui.dragRel(400, 200, duration=1)
    time.sleep(1)
    pyautogui.dragRel(200, 200, duration=1)
    time.sleep(1)
