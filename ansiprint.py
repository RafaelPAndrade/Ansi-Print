#Rafael PAndrade
#18/12/2016

#Ansi-print project
#function to format printing using solely ANSI escape sequences

def aprint(string, *args):
	"""
	Outputs given string according to the arguments given

	Input:
	-string: string to print
	-*args: multiple possible arguments, including:
		-[tuple]colors:white, black, red
		-modes: underlined, italic,...
		-[tuple] a position-(lines, collumns)
	Output:
	-print() with arguments given

	"""

	init='\033['
	#mcodes: ansi sequences related to settings like bold, underline, italic...
	mcodes=init+'0;'

	#ccodes: sequences for coloring
	ccodes=''

	#pcodes:sequences for choosing line and collumn
	pcodes=''

	#Option: if we want to keep the same line; and a status message, if we want anything under the cursor line
	fix_line=False
	status_msg=''


	to_print=''


	modes={'reset':'0', 'bold':'1', 'dim':'2', 'italic':'3', 'underline':'4'}
	colors={'black':'0', 'red':'1', 'green':'2', 'yellow':'3', 'blue':'4', 'magenta':'5', 'cyan':'6', 'white':'7'}

	for setting in args:
		if setting in modes:
		#modes
			mcodes+= modes[setting]+';'
		elif isinstance(setting, tuple) and len(setting)==2:
			if len(setting)==2 and setting[0] in colors:
			#colors
				if setting[0]!=setting[1]:
					ccodes=init+'3'+colors[setting[0]]+';'+'4'+colors[setting[1]]+'m'
				else:
					raise ValueError('aprint: background and foreground colors cannot be the same')


			elif len(setting)==2 and isinstance(setting[0], int):
			#position
				pcodes=init+str(setting[0])+';'+str(setting[1])+'f'


			elif setting[0]=='fix_line':
			#fixing the cursor line on current line
				fix_line= True
				status_msg=str(setting[1])

		elif setting== 'fix_line':
			fix_line= True

	#Format mode codes
	mcodes=mcodes[:-1]+'m'

	#Generating main style string
	to_print=mcodes+ccodes+pcodes+str(string)+'\033[0m'

	#Extra escape sequences to return to the same line+'status' message
	if fix_line== True:
		to_print='\033[s'+to_print+'\033[u'+'\033[2K'+status_msg+'\033[A'+'\033[2K'+'\033[A'


	#2nd step: printing everything
	print(to_print)
	return


def aclear():
	#Clears the screen of all output, returns to the 2nd line counting from the top
	print('\033[2J\033[H')
	return
