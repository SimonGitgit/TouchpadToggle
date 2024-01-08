import subprocess
import time
import pyautogui

# Open the Devices touchpad settings page
s_obj = subprocess.Popen(["start", "ms-settings:devices-touchpad"], shell=True)
# s_obj = os.spawnl

# Delay before pressing the spacebar (if needed)
time.sleep(1)

# Simulate pressing the spacebar
pyautogui.keyDown('space')

# Delay to hold the key down (if needed)
time.sleep(0.05)

# Simulate releasing the spacebar
pyautogui.keyUp('space') 

time.sleep(0.05)