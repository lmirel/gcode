import sys
import time
import math
from os.path import expanduser

def printInstructions():
	helpFile = 'help'
	with open(helpFile) as inGcode:
		helpArray = inGcode.readlines()

	for line in helpArray:
		print(line)

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
 
def sliceTopHalf(inputFile, outputFile, layerNumber):
	print("Writing From Layer Number: " + str(layerNumber))
		
	#Using the newer with construct to close the file automatically.
	with open(inputFile) as inGcode:
		data = inGcode.readlines()

	newGCode = ""
	process = True
	lineNum = 0
	outGcode = open(outputFile,'w')
        lh = 0
        ln = ""
        pl = ""
	for n, line in enumerate(data, 1):
	        #look for command to move Z into position
		if len (line) > 0:
		    #find layer hight on first G0 Za.b line
		    if line.find ('G0') == 0 and line.find (' Z') > 0:
			#print ("Found Z on line: ", line)
			if lh == 0:
			    lh = float (line[ line.find (' Z') + 2 : len (line) ])
			    print "Found layer height: ", str (lh)
			    ln = ' Z' + str (lh * (layerNumber + 1))
			    print "Looking for Z: ", ln
			    process = False #stop writing code
			#lineNum = lineNum + 1
			if len (ln) > 0 and line.find (ln) > 0:
			    print "Found trim line: ", line
			    #raise the print head to needed height to avoid touching the current print
			    outGcode.write (";raise the head to")
			    outGcode.write (ln)
			    outGcode.write ("\n")
			    outGcode.write ("G0")
			    outGcode.write (ln)
			    outGcode.write ("\n")
			    #save the comment from the line above: works for Cura
			    if pl[0] == ';':
				outGcode.write (pl)
			    process = True #start writing code
		#if lineNum == layerNumber and process == False:
		#	outGcode.write("G28 X0 Y0\n")
		#	print ("Found layer: ", str (layerNumber))
		#	process = True
		#store previous line: Cura puts a layer comment on it
		pl = line
		if process == True:
			outGcode.write(line) # python will convert \n to os.linesep
		#elif len(line) > 3 and line[0] != 'G':
		#	outGcode.write(line)
		#	#print ("Writing line: >", line[3], "<")
			
	outGcode.close()
	print("Finished Printing")
	return True

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

