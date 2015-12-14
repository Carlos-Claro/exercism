# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import re

def word_count(phrase):
	phrase = re.sub(r'^[a-z0-9 ]',r'',phrase)
	words = phrase.lower().split()
	count = {}
	for word in words:
		w = str(word)
		count[w] = count.get(word, 0) + 1
	return count
