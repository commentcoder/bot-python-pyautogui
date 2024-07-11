import time
import pyautogui

time.sleep(2)

coords = pyautogui.position()

print(coords, '=', pyautogui.pixel(coords[0], coords[1]))