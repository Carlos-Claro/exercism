
def is_leap_year(var):
	test = False
	if ( var % 4 == 0 ):	
		if ( var % 100 == 0):
			if ( var % 400 == 0):
				test = True
		else:
			test = True 		
	return test


