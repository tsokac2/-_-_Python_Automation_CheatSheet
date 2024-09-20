import pyautogui
import time

position = pyautogui.position()
print(position)
# Point(x=3817, y=583)
pyautogui.doubleClick(3817, 583)
time.sleep(1)
pyautogui.press('down')
pyautogui.press('enter')
pyautogui.write('Python is good to!\n')

pyautogui.hotkey('command', 'a')
pyautogui.hotkey('command', 'c')
pyautogui.press(5*['down'])
pyautogui.hotkey('command', 'v')