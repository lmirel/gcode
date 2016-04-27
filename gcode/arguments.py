#!python
import sys
import math
from os.path import expanduser

def parseArguments():
	#define default argument values
	settings = {
		'layer': 0, 
		'input': expanduser("~") + '\AppData\Local\RepetierHost\composition.gcode',
		'output': expanduser("~") + '\Desktop\output.gcode',
		'help': True
	}

	#iterate command line arguments
	for count, arg in enumerate(sys.argv):
		#rewrite a file starting at a layer number
		if (arg == '-l' or arg == '--layer') and (len(sys.argv) > count + 1):
			settings['layer'] = int(sys.argv[count + 1])
			settings['help'] = False
		#rewrite a file using entered in  dimensions
		elif (arg == '-d' or arg == '--dimensions') and (len(sys.argv) > count + 2):
			#total printed height, measured with caliper
			totalHeight = float(sys.argv[count + 1]);
			#extrusion height in mm
			extrusionHeight = float(sys.argv[count + 2])
			#Add 1 to get rid of the worble
			settings['layer'] = math.ceil(totalHeight / extrusionHeight) + 1
			settings['help'] = False
		#input file
		elif (arg == '-i' or arg == '--input') and (len(sys.argv) > count + 1):
			settings['input'] = sys.argv[count + 1]
		#output file
		elif (arg == '-o' or arg == '--output') and (len(sys.argv) > count + 1):
			settings['output'] = sys.argv[count + 1]
			
	return settings;