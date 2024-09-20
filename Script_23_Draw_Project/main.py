# Your task for this project is to write a Python script that generates 2D plan of a room. You are recommended to use PyAutoGUI to instruct the mouse 
# cursor to draw the plan on https://jspaint.app/ and then use the mss library to take a partial screenshot of the drawing area.

import pyautogui
from mss import mss, tools

start_cordinates = pyautogui.position()
print(start_cordinates)

# Point(x=1931, y=287)
pyautogui.moveTo(1931, 287, duration=1)

pyautogui.click()

dur = 0.1
pyautogui.drag(0, 200, duration=dur, button='left') # Down 200px
pyautogui.drag(60, 0, duration=dur, button='left') # Down - right 60px
pyautogui.drag(0, -3, duration=dur, button='left') # Up 3px
pyautogui.drag(0, 6, duration=dur, button='left')  # Down 6px
pyautogui.drag(60, 0, duration=dur, button='left')
pyautogui.drag(0, -6, duration=dur, button='left')
pyautogui.drag(-60, 0, duration=dur, button='left')

pyautogui.move(60, 0, duration=dur)
pyautogui.move(0, 3, duration=dur)
pyautogui.drag(100, 0, duration=dur, button='left')
pyautogui.drag(0, -120, duration=dur, button='left')

pyautogui.move(0, -40, duration=dur) # Skip 40px
pyautogui.drag(0, -40, duration=dur, button='left')

pyautogui.drag(-220, 0, duration=dur, button='left') # Left 200px
pyautogui.move(-50, 50,)

with mss() as screen:
    part = {'top':277, 'left':1921, 'width':240, 'height':220}
    image = screen.grab(part)
    tools.to_png(image.rgb, image.size, output='src/output.png')