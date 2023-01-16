# set=conjuntos
# se pueden modificar 
# no tienen un orden
# no permite duplicarlos
setCountries={'col', 'mex', 'bol'}
print(setCountries)
print(type(setCountries))

setTypes={1, '1', False, 1.1}
print(setTypes)

setFromString=set('string')
print(setFromString)

setFromTouples=set(('toupleE1', 'toupleE2'))
print(setFromTouples)

numbers=[1,2,3,1,2,3,4]
setNumbers=set(numbers)# Stay with the unique elements thnks at 3rd rule
print(setNumbers)
uniqueNumbers=list(setNumbers)

set_countries = {'col', 'mex', 'bol'}

#len() : Devuelve el tamaño del conjunto
size = len(set_countries)
print(size)

#in, permite sabes si un elemento se encuentra enel conjunto, la expresión se evalua como true si el elemento se encuentra enel conjunto y false si el elemento nose encuentra enel conjunto
print('col' in set_countries)
print('pe' in set_countries)

# add(): Añade un elemento al conjunto.
set_countries.add('pe')
print(set_countries)
set_countries.add('pe')
print(set_countries)

# update(): Añade cualquier tipo de objeto iterable como: listas, tuplas
set_countries.update({'ar', 'ecua', 'pe'})
print(set_countries)

# remove(): Elimina un elemento y si este no existe lanza el error “keyError”
set_countries.remove('col')
print(set_countries)
set_countries.remove('ar')

#discard(): Elimina un elemento y si ya existe no lanza ningún error
set_countries.discard('arg')
print(set_countries)
set_countries.add('arg')
print(set_countries)

#pop(): Nos devuelve un elemento aleatorio ylo elimina y si el conjunto está vacío lanza el error “key error”.
print(set_countries.pop())
print(set_countries)

#clear(): Elimina todo el contenido del conjunto
set_countries.clear()
print(set_countries)
print(len(set_countries))
