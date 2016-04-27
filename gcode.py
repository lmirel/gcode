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
showHelp = True
for count, arg in enumerate(sys.argv):
	#Rewrite a file starting at a layer number
	if (arg == '-l' or arg == '--layer') and (len(sys.argv) > count + 1):
		#Add 1 to get rid of the worble
		layerNumber = sys.argv[count + 1]	
		showHelp = False
	#Rewrite a file using entered in  dimensions
	elif (arg == '-d' or arg == '--dimensions') and (len(sys.argv) > count + 2):
		totalHeight = float(sys.argv[count + 1]);
		extrusionHeight = float(sys.argv[count + 2])
		layerNumber = math.ceil(totalHeight / extrusionHeight) + 1
		showHelp = False

if showHelp == True:
	print("+------------------------------------------------------------------+")
	print("| GCode Repair Tool                                                |")
	print("+------------------------------------------------------------------+")
	print("| The purpose of this program is to resume a print that has        |")
	print("| previously died.                                                 |")
	print("|                                                                  |")
	print("| If you know the layer number where the print                     |")
	print("| died at, you resume printing at that layer.                      |")
	print("|                                                                  |")
	print("| If you don't have which layer the print stopped at you can take  |")
	print("| the total prited height of your object on the print bed (in mm)  |")
	print("| followed by the extrusion height of the print in milimeters.     |")
	print("+------------------------------------------------------------------+")
	print("|                                                                  |")
	print("| Syntax:                                                          |")
	print("|    gcode.py <argument>                                           |")
	print("| Arguments:                                                       |")
	print("|     --dimensions, -d:                                            |")
	print("|          -d <total_height> <extrusion_height>                    |")
	print("|     --layer, -l:                                                 |")
	print("|          -l <layer_number>                                       |")
	print("+------------------------------------------------------------------+")
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