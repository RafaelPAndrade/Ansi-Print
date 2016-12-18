#Rafael PAndrade
#18/12/2016

#ANSI Color Codes:
#Color:		|Foreground	|Background
#Black		|30		|40
#Red		|31		|41
#Green		|32		|42
#Yellow		|33		|43
#Blue		|34		|44
#Magenta	|35		|45
#Cyan		|36		|46
#White		|37		|47


#ANSI printing modes:
#(There are more)
#Off=0
#Bold=1
#Underscore=4
#Blink=5
#Reverse=7
#Concealed=8


#ANSI Color Syntax:
#
#    \033[<mode>;3<color number>;4<color number>m
#
#where:
#-3 stands for the foreground (font) color
#-4 stands for the background (screen) color

def cprint(string, mode=0, colorf=7, colorb=0):
	"""
	Prints colored output on terminal sessions
	
	Input:
	-string: text to be written on screen
	-mode: ansi mode (default-off)
	-colorf: foreground (font) color (default-white) 
	-colorf: background (screen) color (default-white) 
	
	Output:
	-Prints <strings> with specified colors
	"""
	
	argument='\033['+str(mode)+';3'+str(colorf)+';4'+str(colorb)+'m'
	
	print(argument+string)
	return

