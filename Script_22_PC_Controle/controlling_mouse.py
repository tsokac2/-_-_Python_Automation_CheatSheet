import pyautogui

position = pyautogui.position()
print(position)

# pyautogui.moveTo(3758, 521, duration=1)
# pyautogui.move(100, 0, duration=1)

# pyautogui.moveTo(3758, 521, duration=1)
# pyautogui.click(clicks=2)

# pyautogui.click(3758, 521)

# pyautogui.click(3758, 521, button='right')

# # RIGHT-CLICK ON MAC
# pyautogui.click(3758, 521)
# pyautogui.dragTo(3758, 521, button='right')

pyautogui.moveTo(2099,467, duration=1)
pyautogui.click()
pyautogui.drag(150, 0, duration=1, button='left')
pyautogui.drag(0, -150, duration=1, button='left')
pyautogui.drag(-150, 0, duration=1, button='left')
pyautogui.drag(0, 150, duration=1, button='left')