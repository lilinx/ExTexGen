# -*- coding: utf-8 -*-
#!/usr/bin/python
from random import choice
import webbrowser

print 'ExTexGen by Pierre Chevalier - 2013 - Method 1' 
verses = "excitacumtremulisanusattulitartubuslumen"
x = ""
z = 1
best = ""
boucle = 1
while True:
	z = z + 1
	if x in verses[:len(x)]:
		if len(x) > len(best):
			best = x
			print z , 'letters thrown on the floor'
			print best , 'is the best result so far'
			webbrowser.open('http://translate.google.com/translate_tts?tl=la&q=' + best, new=0)
		x = x + (choice('abcdefghilmnopqrstuvx'))
	else:
		x = ""
