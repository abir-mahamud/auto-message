import pyautogui
import time
text = 5
while text > 0:
    time.sleep(4)
    pyautogui.typewrite('have a safe journey' )
    pyautogui.press('enter')
    text = text - 1
pyautogui.typewrite('Pouchaiya janaiyen')
pyautogui.press('enter')