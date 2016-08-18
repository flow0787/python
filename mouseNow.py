#! python3
# mouseNow.py - Displays the mouse cursor's current position.

import pyautogui

print('Press CTRL+C to quit.')

try:
	while True:
		# Get and print the mouse coordinates
		x, y = pyautogui.position()
		positionStr = 'x: ' + str(x).rjust(4) + ' y: ' + str(y).rjust(4)
except KeyboardInterrupt:
	print('\nDone.')