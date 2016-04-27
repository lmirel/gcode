#!python
 
def sliceTopHalf(inputFile, outputFile, layerNumber):
	print("Writing From Layer Number: " + str(layerNumber))
		
	#Using the newer with construct to close the file automatically.
	with open(inputFile) as inGcode:
		data = inGcode.readlines()

	newGCode = ""
	process = False
	lineNum = 0
	outGcode = open(outputFile,'w')

	for n, line in enumerate(data, 1):
		if len(line) > 3:
			if line[3] == 'Z':	
				lineNum = lineNum + 1
				
		if lineNum == layerNumber and process == False:
			outGcode.write("G28 X0 Y0\n")
			process = True
			
		if process == True:
			outGcode.write(line) # python will convert \n to os.linesep
		elif len(line) > 3 and line[0] != 'G':
			outGcode.write(line)
			
	outGcode.close()
	print("Finished Printing")
	return True