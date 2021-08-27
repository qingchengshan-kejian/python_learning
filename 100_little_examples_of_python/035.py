#!/usr/bin/python
# -*- coding:UTF-8 -*-

class bcolors:
	HEADER='\033[95m'
	OKGREEN='\033[92m'
	WARNING='\033[93m'
	FAIL='\033[91m'
	ENDC='\033[0m'
	BOLD='\033[1m'
	UNDERLINE='\033[4m'
print (bcolors.WARNING + 'the warning color?'+bcolors.ENDC)		
print (bcolors.FAIL+ 'the faile color?' + bcolors.ENDC)