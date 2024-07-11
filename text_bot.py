import time
import pyautogui

time.sleep(2)

x = 809
y_start = 415
y_step = 457 - 415

while True:
im = pyautogui.screenshot(region=(675, 398, 772 - 675, 699 - 398))

lines = pytesseract.image_to_string(im)

lines = res.strip() \
    .replace('/20', '') \
    .replace('/ 20', '') \
    .replace('[20', '') \
    .split('\n')

is_over = True
for i, line in enumerate(lines):
    for _ in range(20 - int(line)):
      pyautogui.click(x, y_start + y_step * i)
      is_over = False

  if is_over == True:
    quit()
