# union(set): Realiza la operacion “union” entre dos conjuntos. 
#           La unión entre dos conjuntos es sumar los elementos de estos sin repetir elementos. 
#           Esta operación tambien se puede realizar con el signo “|”: set_a | set_b.
# intersection(set): Realiza la operacion “intersection” entre dos conjuntos. 
#                   La intersección entre dos conjuntos es tomar unicamente los elementos en común de 
#                   los conjutnos. Esta operación tambien se puede realizar con el signo “&”: set_a & set_b.
# difference(set): Realiza la operacion “difference” entre dos conjuntos. 
#               La diferencia entre dos conjuntos es restar los elementos del segundo conjunto al primero. 
#               Esta operación tambien se puede realizar con el signo “-”: set_a - set_b.
# symmetric_difference(set): Realiza la operacion “symmetric_difference” entre dos conjuntos. 
#                           La diferencia simetrica entre dos conjutnos consta de restar todos los elementos 
#                           de ambos exceptuando el elemento en común. Esta operación tambien se puede realizar 
#                           con el signo “^”: set_a ^ set_b.

setA={'E1','E2','E3'}
setB={'E4','E3'}

setC=setA.union(setB)
print(setC)
print(setA | setB)

setC=setA.intersection(setB)
print(setC)
print(setA & setB)

setC=setA.difference(setB)
print(setC)
print(setA - setB)

setC=setA.symmetric_difference(setB)
print(setC)
print(setA ^ setB)

# Para resolver este desafío, debes escribir un algoritmo que elimine los elementos repetidos para obtener un conjunto único llamado new_set.
# Este algoritmo recibirá como entrada cuatro conjuntos de países, estos países serán de todo el continente americano divididos de la siguiente manera:
#     countries - Países del continente en general.
#     northAmerica - Países del norte de América.
#     centralAmerica - Países del centro de América.
#     southAmerica - Países del sur de América.
# En resumen, el algoritmo deberá eliminar los elementos repetidos de los cuatro conjuntos de países y obtener un conjunto único llamado new_set.
# Ejemplo 1:
# Input: 
# {"MX", "COL", "ARG", "USA"},
# {"USA", "CA"},
# {"MX", "GT", "BZ"},
# {"COL", "BZ", "ARG"}

# Output:
# {'ARG', 'USA', 'CANADA', 'GT', 'COL', 'MX', 'BZ'}
# Ejemplo 2
# Input:
# {"BOL"},
# {"CA"},
# {"MX"},
# {"COL"}

# Output:

# {'COL', 'CA', 'BOL', 'MX'}


countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}

new_set = countries.union(northAm,centralAm,southAm)

print(new_set)