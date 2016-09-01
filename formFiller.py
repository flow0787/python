#! python
# formFiller.py - Automatically fills in the form.

import pyautogui, time

nameField = (693, 303)
submitButton = (688, 783)
submitButtonCollor = (75, 141, 249)
submitAnotherLink = (798, 213)

formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand', 'robocop': 1, 'comments': 'Tell bob I said hi.'},
			{'name': 'Florin', 'fear': 'stupidity', 'source': 'amulet', 'robocop': 4, 'comments': 'Al help me learn coding pleaaaaseee!'},
			{'name': 'Jim', 'fear': 'dorks', 'source': 'crystal ball', 'robocop': 3, 'comments': 'rock on!'},
			{'name': 'Spiderman', 'fear': 'crocodiles', 'source': 'money', 'robocop': 2, 'comments': 'spidey sense!'},]

# Wait 0.5 seconds after each function call
pyautogui.PAUSE = 0.5

try:

	for person in formData:
		# Give the user a chance to kill the script.
		print('>>> 5 SECOND PAUSE TO LET USER PRESS CTRL-C <<<')
		time.sleep(5)

		# Wait until the form page has loaded.
		#while not pyautogui.pixelMatchesColor(submitButton[0], submitButton[1], submitButtonCollor):
			#time.sleep(0.5)

		print('Entering %s info...' % (person['name']))
		pyautogui.click(nameField[0], nameField[1])
		
		# Fill out the Name field.
		pyautogui.typewrite(person['name'] + '\t')
		# Fill out the "Greatest Fear" field.
		pyautogui.typewrite(person['fear'] + '\t')
		
		# Fill out the "source of wizzard powers" drop down.
		if person['source'] == 'wand':
			pyautogui.typewrite(['down'])
			pyautogui.typewrite('\t')
		elif person['source'] == 'amulet':
			pyautogui.typewrite(['down', 'down'])
			pyautogui.typewrite('\t')
		elif person['source'] == 'crystal ball':
			pyautogui.typewrite(['down', 'down', 'down'])
			pyautogui.typewrite('\t')
		elif person['source'] == 'money':
			pyautogui.typewrite(['down', 'down', 'down', 'down'])
			pyautogui.typewrite('\t')

		# Pick a radio button "robocop was the greatest movie in the '90s"
		if person['robocop'] == 1:
			pyautogui.typewrite(' ')
			pyautogui.typewrite('\t')
		elif person['robocop'] == 2:
			pyautogui.typewrite(['right'])
			pyautogui.typewrite('\t')
		elif person['robocop'] == 3:
			pyautogui.typewrite(['right', 'right'])
			pyautogui.typewrite('\t')
		elif person['robocop'] == 4:
			pyautogui.typewrite(['right', 'right', 'right'])
			pyautogui.typewrite('\t')
		elif person['robocop'] == 5:
			pyautogui.typewrite(['right', 'right', 'right', 'right'])
			pyautogui.typewrite('\t')

		# Fill out the "additional comments" field.
		pyautogui.typewrite(person['comments'] + '\t')

		# click submit.
		pyautogui.click(submitButton[0], submitButton[1])

		# Wait until t he form page has loaded.
		print('Clicked submit.')
		time.sleep(5)

		# Click the submit another response link.
		pyautogui.click(submitAnotherLink[0], submitAnotherLink[1])
except KeyboardInterrupt:
	print('Script terminated.')