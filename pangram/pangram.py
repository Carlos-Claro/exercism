# -*- coding: utf-8 -*-

import string

def is_pangram( phrase ):
	alfabeto = list(string.ascii_lowercase);
	phrase = phrase.lower()
	for letra in phrase :
		for a in alfabeto :
			if ( letra == a): 
				 alfabeto.remove(a)
	if ( len(alfabeto) == 0 ):
		return True
	else:
		return False

