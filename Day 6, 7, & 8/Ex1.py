import pyautogui
import time

pyautogui.keyDown('command')
pyautogui.press('space')
pyautogui.keyUp('command')
pyautogui.write('chrome')
pyautogui.press('enter')

pyautogui.keyDown('command')
pyautogui.press('t')
pyautogui.keyUp('command')

pyautogui.write('mail.google.com')
pyautogui.press('enter')
time.sleep(5)

pyautogui.click(x = 75, y = 175)
time.sleep(1)
pyautogui.write('ee331@cam.ac.uk')
pyautogui.press('enter')
time.sleep(1)

pyautogui.click(x = 1000, y = 500)
pyautogui.write('I am not the first.')
pyautogui.keyDown('command')
pyautogui.press('enter')
pyautogui.keyUp('command')