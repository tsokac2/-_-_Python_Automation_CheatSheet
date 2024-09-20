from mss import mss

with mss() as screen:
    screen.shot(output='src/screenshot.png')