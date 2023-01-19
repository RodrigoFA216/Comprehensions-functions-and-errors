# Array=[Element Loop where extracts elements of any iterable loop]
# Array=[element for element in iterable]
numbers=[]
for elements in  range(1,10):
    numbers.append(elements*2)
print(numbers)

numbersV2=[element*2 for element in range(1,10)]
print(numbersV2)

# Array=[Element |Loop where extracts elements of any iterable loop |Optional condition for filter elements]
# Array=[Element for Element in iterable if condition]
numbersV3=[]
for elements in  range(1,10):
    if elements%2==0:
        numbersV3.append(elements*2)
print(numbersV3)

numbersV4=[element*2 for element in range(1,10) if element%2==0]
print(numbersV4)