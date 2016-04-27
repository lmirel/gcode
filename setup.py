from setuptools import setup, find_packages

setup(name='gcode',
      version='0.2.0',
      packages=find_packages(),
	  py_modules = [
            'gcode.arguments', 
            'gcode.instructions',
			'gcode.slicer',
            ],
      entry_points={
          'console_scripts': [
              'gcode = gcode.__main__:main'
          ]
      },
      )