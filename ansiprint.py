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

	#1st step: create necessary ansi codes
	init='\033['
	mcodes=init+'0;'
	ccodes=''
	pcodes=''
	
	colors={'black':'0', 'red':'1', 'green':'2', 'yellow':'3', 'blue':'4', 'magenta':'5', 'cyan':'6', 'white':'7'}
	modes={'reset':'0', 'bold':'1', 'dim':'2', 'italic':'3', 'underline':'4'}

	for setting in args:
		if setting in modes:
		#modes
			mcodes+= modes[setting]+';'
		elif isinstance(setting, tuple) and len(setting)==2:
			if setting[0] in colors:
			#colors
				if setting[0]!=setting[1]:
					ccodes=init+'3'+colors[setting[0]]+';'+'4'+colors[setting[1]]+'m'
				else:
					raise ValueError('aprint: background and foreground colors cannot be the same')
			elif isinstance(setting[0], int):
			#position
				pcodes=init+str(setting[0])+';'+str(setting[1])+'f'
				#codes=codes
	
	mcodes=mcodes[:-1]+'m'

	#2nd step: printing the ansi codes+string+reset
	print(mcodes+ccodes+pcodes+str(string)+'\033[0m')
	return


#A way to print a thing and comeback to previous line (except last line)
#>>> print(save_cursos+<anything generated>+rest_cursor+<text under the prompt>+'\033[1A'+'\033[K'+'\033[1A')
