import time
import pyautogui

time.sleep(2)

while True:
  try:
    mole = pyautogui.locateCenterOnScreen(
      'images/taupe.png',
      region=(554 * 2, 356 * 2, (1117 - 554) * 2, (870 - 356) * 2),
      grayscale=True,
      confidence=0.6
    )

    pyautogui.click(mole[0] / 2, mole[1] / 2)
  except pyautogui.ImageNotFoundException:
    print("Image pas trouvée")
  
  time.sleep(0.5)