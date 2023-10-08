import pyautogui
from time import sleep
from random import choice

# pyautogui.size()
# pyautogui.position()


lst = ["Hello", "Hi", "i am robot", "Fariba"]
for i in range(4):
    sleep(1)
    pyautogui.click(410, 986)
    pyautogui.write(choice(lst), interval=0.1)
    pyautogui.hotkey('shift', 'enter')

pyautogui.press("enter")
