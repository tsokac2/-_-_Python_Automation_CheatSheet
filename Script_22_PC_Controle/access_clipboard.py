import pyautogui
import pyperclip
import time

position = pyautogui.position()
print(position)

pyautogui.doubleClick(3817, 583)
pyautogui.hotkey('command', 'a')
pyautogui.hotkey('command', 'c')

text = pyperclip.paste()
pyautogui.alert(text)
print(text)