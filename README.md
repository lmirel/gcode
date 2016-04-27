# Welcome to my gcode tool for restarting 3d prints where they stopped printing
Normally when you print something on your 3d printer, if your printer stops, you computer shuts down, or your head stops extruding, you have to restart your print. 

I created this utility so that if you have the gcode file of your print that stopped, you can measure it's height and continue printing where it left off.

## Installation Requirements
You have to have python installed and add the python installation directories to your PATH.

## Install
> git clone https://github.com/jensenj08/gcode 
> python gcode/setup.py install

## Usage
### I know the line that the print was on when it stopped 
This example is for when the print stopped when it was on line 10
> gcode -l 10

### I don't know the line number where the print stopped 
This example shows when we don't know the line number that the print was on, but we do know that the print is currently 12.14mm tall, and the extrusion height is set to .4mm
> gcode -d 12.14 0.4