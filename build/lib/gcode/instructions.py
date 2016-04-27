#!python 

def printInstructions():
	helpFile = 'help'
	with open(helpFile) as help:
		helpArray = inGcode.help()

	for line in helpArray:
		print(line)