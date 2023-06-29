#!/usr/bin/python3

### Simple Timer Terminal Application ###

"""
Author: Aaron 
Start Date: 9/27/21
Encoding: UTF-8
python 3.9

Description: 
Super Basic timer cli application so that I don't have to use the windows app on PC lol. 
"""


try: 
	import sys
	import colorama
	import time
	import math
	from colorama import Fore, Back, Style
except:	
	print(Fore.RED + "ERROR: Could not import all necessary libraries.")


mins = sys.argv[1]		# User entered time in minutes
# flag = sys.argv[2, ~]		# User entered flag for specified functionalitiy 

Line_Flush = '\r\033[K'
Up_Front_Line = '\033[F'


# Flags that could be useful: 
# 	-ng : for "quiet running clock" -> no graphic until times up
# 	-q : on time up no bell, will show end state text



def main(timeInMins):
	timeInMins = int(timeInMins)
	timeInSecs = timeInMins * 60
	print("Time Remaining: ")
	print(" ")

	for i in range(0,int(timeInSecs)):
		if(timeInSecs - i) >= 120: 
			print(Up_Front_Line + str(math.floor((timeInSecs - i) / 60)) + " Minutes and " + str((timeInSecs - i) % 60) + " seconds    ")
			time.sleep(1)
		elif 120 >(timeInSecs - i) > 60:
			print(Up_Front_Line + str(math.floor((timeInSecs - i) / 60)) + " Minute and " + str((timeInSecs - i) % 60) + " seconds    ")
			time.sleep(1)
		elif 60 >= (timeInSecs - i) > 10:
			print(Up_Front_Line + str(timeInSecs - i) + " seconds                                               ")
			time.sleep(1)
		else: 
			print(Up_Front_Line + str(timeInSecs - i) + " seconds                                               ")
			time.sleep(1)

	print(Up_Front_Line)
	if int(timeInMins) == 1:
		print(Up_Front_Line + '\a' + str(timeInMins) + " Minute elapsed")
	else: 
		print(Up_Front_Line + '\a' + str(timeInMins) + " Minutes elapsed")

	### Add sound effect here


try:
	main(mins)
except: 
	print(Fore.RED + "ERROR: Computer says no")