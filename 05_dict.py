# dictionary={key:value for var in iterable}
# variable={Key value Element |loop where generate elements that will be extracted from any iterable}
dict={}
for i in range(1,5):
    dict[i]=i*2
print(dict)

dictV2={i:i*2 for i in range(1,5)}
print(dictV2)

# dictionary={key:value for var in iterable conditional}
# variable={Key value Element |loop where generate elements that will be extracted from any iterable}

dictV3={}
for i in range(1,5):
    if i%2==0:
        dictV3[i]=i*2
print(dictV3)

dictV4={i:i*2 for i in range(1,5) if i%2==0}
print(dictV4)

# Doing this bt for a object person
keys=('name', 'lastname', 'age', 'languajes')
names=['Rodrigo','Flores', 24, ['python', 'c++', 'js']]
dictV5={keys[i]:names[i] for i in range(len(names))}
print(dictV5)

# we can do this bt with function zip
keys=('name', 'lastname', 'age', 'languajes')
names=['Rodrigo','Flores', 24, ['python', 'c++', 'js']]
dictV6={key:name for (key,name) in zip(keys,names)}
print(dictV6)

import random as rand
countries=['col', 'mex', 'bol', 'arg']
dictV7={country:rand.randint(1,20) for country in countries}
print(dictV7)
# Filter the countries that have number more than 10
result={country:population for (country,population)in dictV7.items()if population>10}
print(result)

#do a dictionary with the count of vowels in the phrase
text='Hi how are you?'
unique={c.upper():text.count(c) for c in text if c in 'aeiou'}
print(unique)