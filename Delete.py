import pyautogui
import time
cont = 0
while cont < 20:
    time.sleep(2)
    pyautogui.moveTo(400, 400)
    pyautogui.click(400, 400)
    pyautogui.hotkey('End')
    time.sleep(4)
    pyautogui.hotkey('End')
    time.sleep(4)
    pyautogui.hotkey('Ctrl', 'Shift', 'A')
    pyautogui.hotkey('Del')
    time.sleep(1)
    pyautogui.hotkey('Enter')
    time.sleep(10)
    pyautogui.hotkey('F5')
    cont += 1
