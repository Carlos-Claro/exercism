
def on_square(num, ret = False):
	square = 0
	prev_square_count = 0
	count = 0
	acumulado = 0
	while count < num :
		square += 1
		if ( prev_square_count == 0 ) :
			prev_square_count = 1
		else :
			prev_square_count = 2 * prev_square_count
		count += 1
		acumulado = acumulado + prev_square_count
	if ( ret == False ) :
		return prev_square_count
	else :
		return acumulado

def total_after(num):
	acumulado = on_square(num, True)
	return acumulado
	
