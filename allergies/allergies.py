def Allergies( qtde ):
	conjunto = ['eggs','peanuts','shellfish','strawberries','tomatoes','chocolate','pollen','cats']
	valores = []
	a = 1
	for conj in conjunto :
		a = a * 2
		valores[a] = conj
	return valores[qtde]
		
