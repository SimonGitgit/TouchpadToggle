import subprocess
import time
import pyautogui

# Open the Devices touchpad settings page
subprocess.Popen(["start", "ms-settings:devices-touchpad"], shell=True)

# Delay before pressing the spacebar (if needed)
time.sleep(1)

# Simulate pressing the spacebar
pyautogui.keyDown('space')

# Delay to hold the key down (if needed)
time.sleep(0.05)

# Simulate releasing the spacebar
pyautogui.keyUp('space') 