import time
import pyautogui

time.sleep(2)

while True:
  try:
    mole = pyautogui.locateCenterOnScreen(
      'images/taupe.png',
      region=(554, 356, 1117 - 554, 870 - 356),
      grayscale=True,
      confidence=0.6
    )

    pyautogui.click(mole[0], mole[1])
  except pyautogui.ImageNotFoundException:
    print("Image pas trouvée")
  
  time.sleep(0.5)
