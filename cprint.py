#Rafael PAndrade
#18/12/2016

#ANSI Color Codes:
Black=0
Red=1
Green=2
Yellow=3
Blue=4
Magenta=5
Cyan=6
White=7


#ANSI printing modes:
Off=0
Bold=1
Underscore=4
Blink=5
Reverse=7
Concealed=8


#ANSI Syntax:
#
#    \033[<mode>;3<color number>;4<color number>m
#
#where:
#-3 stands for the foreground (font) color
#-4 stands for the background (screen) color



def cprint(colorf=7, colorb=0, mode=1, *strings):
	"""
	Prints colored output on terminal sessions
	
	Input:
	-*strings- zero or more strings
	-colorf, colorb- one of the seven ANSI colors; colorf is foreground 
and colorb is background
	-mode: ansi mode, default (in chrome os) is 1
	
	
	Output:
	-Prints <strings> with specified colors
	"""
	
	argument='\033['+str(mode)+';3'+str(colorf)+';4'+str(colorb)+'m'
	
	for string in strings:
		print(argument+string)
	return

