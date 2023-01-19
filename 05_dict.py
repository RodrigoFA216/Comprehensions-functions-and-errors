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
names=('Rodrigo','Alfredo','Mara','Amy')
names2=('Rodrigo','Alfredo','Mara','Amy')
dictV5={alfa:name for name in names for alfa in names2 }
print(dictV5)