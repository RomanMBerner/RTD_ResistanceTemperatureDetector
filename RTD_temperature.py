# #######################################################
# python script to read the platinum RTD converter	#
# Last modifications: 28.11.2018 by R.Berner		#
#########################################################

#!/usr/bin/python
import time, math
import subprocess

if __name__ == "__main__":

	import max31865

	# Define pins:
	cs0Pin	=	 5
	#cs1Pin	=	 6
	#...

	misoPin	=	 9
	mosiPin	=	10
	clkPin	=	11

	sens0 = max31865.max31865(cs0Pin,misoPin,mosiPin,clkPin,0)
	#sens1 = max31865.max31865(cs1Pin,misoPin,mosiPin,clkPin,1)
	#...

        while 1:
            time.sleep(0.1)
            tempC = sens0.readTemp()
            #tempC = sens1.readTemp()
            #...
            print "\n"

	GPIO.cleanup()
