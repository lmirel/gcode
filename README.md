# Welcome to my gcode tool for restarting 3d prints where they stopped printing
Normally when you print something on your 3d printer, if your printer stops, you computer shuts down, or your head stops extruding, you have to restart your print. 

I created this utility so that if you have the gcode file of your print that stopped, you can measure it's height and continue printing where it left off.

This utility default locations work by default with repetier host.

## Installation Requirements
You have to have [python](https://www.python.org/downloads/) installed and add the python installation directories to your PATH.

## Install
### Manual installation
Run these commands to install the ulility: 
```
git clone https://github.com/jensenj08/gcode 
python gcode/setup.py install
```
### Using Python's pip
```
pip install gcode
```

## Usage
### I know the line that the print was on when it stopped 
If the print stopped printing at line 10, run this command:
```
gcode -l 10
```

### I don't know the line number where the print stopped 
If your print was 12.14mm tall when it stopped, and the extrusion height is set to .4mm, then run this command.
```
gcode -d 12.14 0.4
```

### The output
These commands will output a file onto your desktop called output.gcode. Load this file into your 3d printer and your print will resume where it left off.