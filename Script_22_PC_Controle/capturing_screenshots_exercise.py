# Write a program that captures screenshots every 10 minutes 
# and saves them in the project directory as PNG files. 
# Optionally, you can instruct the program to save the screenshots using timestamps as filenames. For example:

# 2022-02-02 13:17:21.png
# 2022-02-02 13:27:21.png
# 2022-02-02 13:37:21.png
# etc.

from mss import mss
import time
from datetime import datetime
 
# Set interval (600 sec = 10 min)
interval = 600
 
while True:
    with mss() as screen:
        # Filepath will have the current datetime (e.g., 2022-02-02 13:17:21.png)
        filepath = f"{datetime.now().strftime('%Y-%m-%m %H:%M:%S')}.png"
        screen.shot(output=filepath)
 
    print(filepath)
    time.sleep(interval) # Wait 600 sec/ 10 min