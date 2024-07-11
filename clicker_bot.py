import time
import pyautogui

time.sleep(2)

gift_pos = (579, 513)

purchasable_color = (41, 44, 51)

x = 1345
upgrades_y = [493, 583, 670, 756]

while True:
  for i in range(20):
    pyautogui.click(gift_pos[0], gift_pos[1])

  for y in upgrades_y[::-1]:
    if pyautogui.pixel(x, y) == purchasable_color:
      pyautogui.click(x, y)
