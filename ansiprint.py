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
		-[tuple] a position-(lines, collumns) #not implemented
	Output:
	-print() with arguments given
	
	"""

	#1st step: create necessary ansi codes
	codes='\033['
	
	#ccodes: color related codes are concatenated on a single escape sequence
	ccodes=codes
	
	
	colors={'black':'0', 'red':'1', 'green':'2', 'yellow':'3', 'blue':'4', 'magenta':'5', 'cyan':'6', 'white':'7'}
	modes={'reset':'0', 'bold':'1', 'dim':'2', 'italic':'3', 'underline':'4'}

	for setting in args:
		if setting in modes:
			ccodes+= modes[setting]+';'
		elif isinstance(setting, tuple) and len(setting)==2:
			if setting[0] in colors:
			#colors
				if setting[0]!=setting[1]:
					ccodes+= '3'+colors[setting[0]]+';'+'4'+colors[setting[1]]+';'
				else:
					raise ValueError('aprint: background and foreground colors cannot be the same')
			else:
			#position
				codes=codes
	
	ccodes=ccodes[:-1]+'m'
	#2nd step: printing the ansi codes+string+resetting ansi codes
	print(ccodes+str(string)+'\033[0m')
	return

