#!python 
import time 
import sys
import math
from os.path import expanduser
home = expanduser("~") + '\AppData\Local\RepetierHost\composition.gcode'

gcodeFile = home
outputFile = expanduser("~") + '\Desktop\output.gcode'

#The layer to start pringing at
layerNumber = 1
argFound = False
for count, arg in enumerate(sys.argv):
	if arg == '-l':
		#Add 1 to get rid of the worble
		layerNumber = sys.argv[count + 1]	
		argFound = True
	elif arg == '-h':
		if len(sys.argv) > count + 2:
			totalHeight = float(sys.argv[count + 1]);
			extrusionHeight = float(sys.argv[count + 2])
			layerNumber = math.ceil(totalHeight / extrusionHeight) + 1
			argFound = True

if argFound == False:
	print("Syntax: gcode.py (-l <layer_number>)|(-h <measured_height> <extrusion_height>)")
	sys.exit()
	

print("Writing From Layer Number: " + str(layerNumber))
	
#Using the newer with construct to close the file automatically.
with open(gcodeFile) as f:
    data = f.readlines()

newGCode = ""
process = False
lineNum = 0
f = open(outputFile,'w')

for n, line in enumerate(data, 1):
	if len(line) > 3:
		if line[3] == 'Z':	
			lineNum = lineNum + 1
			
	if lineNum == layerNumber and process == False:
		f.write("G28 X0 Y0\n")
		process = True
		
	if process == True:
		f.write(line) # python will convert \n to os.linesep
	elif len(line) > 3 and line[0] != 'G':
		f.write(line)
f.close()
print("Finished Printing")