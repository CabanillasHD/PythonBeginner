import pyautogui
import time
cont = 0
while cont < 30:
    time.sleep(15)
    pyautogui.click(400, 400)
    pyautogui.hotkey('End')
    pyautogui.hotkey('End')
    pyautogui.hotkey('End')
    time.sleep(20)
    pyautogui.hotkey('End')
    pyautogui.hotkey('End')
    pyautogui.hotkey('End')
    time.sleep(20)
    pyautogui.hotkey('Ctrl', 'A')
    pyautogui.hotkey('Del')
    time.sleep(1)
    pyautogui.click(860, 474)
    time.sleep(7)
    pyautogui.hotkey('F5')
    cont += 1
