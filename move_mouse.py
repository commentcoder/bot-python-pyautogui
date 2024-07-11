import time
import pyautogui

time.sleep(2)

origin = (743, 348)

temp_y = 792
temp_x = 805

distance_x = temp_x - origin[0]
distance_y = temp_y - origin[1]

pyautogui.moveTo(origin[0], origin[1])
pyautogui.move(0, distance_y, 0.7)
pyautogui.move(distance_x, 0, 0.1)
pyautogui.move(0, -distance_y, 0.7)
pyautogui.move(distance_x, 0, 0.1)
pyautogui.move(0, distance_y, 0.7)
pyautogui.move(distance_x, 0, 0.1)
pyautogui.move(0, -distance_y, 0.7)
pyautogui.move(distance_x, 0, 0.1)
pyautogui.move(0, distance_y, 0.7)