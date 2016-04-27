#!python 
from gcode.instructions import *
from gcode.arguments import *
from gcode.slicer import *
import time
import math
from os.path import expanduser

def main():
	settings = parseArguments()

	#print help file
	if settings['help'] == True:
		printInstructions()
		sys.exit()
	#re-slice g-code file to only include top half of print
	sliceTopHalf(settings['input'], settings['output'], settings['layer'])

if __name__ == "__main__":
    main()