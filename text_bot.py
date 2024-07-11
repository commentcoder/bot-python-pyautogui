import time
import pyautogui

time.sleep(2)
  
im = pyautogui.screenshot(region=(675, 398, 772 - 675, 699 - 398))
im.save('rose.png')
