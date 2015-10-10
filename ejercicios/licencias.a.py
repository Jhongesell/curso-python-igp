#!/usr/bin/env python //Evita que le pongamos al archivo la extension .py
# -*- coding: utf8 -*-

import string
import random
import sys
import os
os.system('clear')

alfa=string.digits+string.ascii_uppercase
cont=0
for i in range(int(sys.argv[1])):
	str=''
	cont=0
	for a in range(0,25):
		cont+=1
		str+=(alfa[random.randint(0,len(alfa)-1)])
		if(cont <25 and cont%5 == 0):
			str+='-'
	print str
