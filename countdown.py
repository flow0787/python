# contdown.py - A simple countdown script.

import time, subprocess

timeleft = 3
while timeleft > 0:
	print(timeleft)
	time.sleep(1)
	timeleft -= 1
# At the end of the coundown, play a sound file.
subprocess.Popen(['open','alarm.wav'])