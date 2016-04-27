#!python 
from instructions import *
from arguments import *
from slicer import *
import time
import math
from os.path import expanduser

settings = parseArguments()

#print help file
if settings['help'] == True:
	printInstructions()
	sys.exit()

#re-slice g-code file to only include top half of print
sliceTopHalf(settings['input'], settings['output'], settings['layer']);