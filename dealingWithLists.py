'''
Lists, manipulate, modifying, inserting, delete and organisation


countries = ['ghana', 'benin', 'togo', 'angola', 'nigeria', 'senegal', 'gabon']
ages = [3, 5, 2, 45, 6, 3, 5, 23, 5, 3]
print(countries)
#print(countries[1])
#print(countries[2])

#print(countries[-1])
#print(countries[-2].title())

#print("Kofi is " + str(ages[3]) + " years old. \nHe is from " + countries[-2].title())
#print("He is from " + countries[-2].title())


#Modifying element in the list
countries[0] = 'Congo'
countries[-1] = 'Tunisia'
print(countries)

#Insert element to the list
countries.insert(0, 'South Africa')
countries.insert(-1, 'Zambia')
print(countries)

#appending element to the list
countries.append('Morocco')
print(countries)

#delete (del, pop, remove) element from the list
del countries[0]
print(countries)

deleteCountry = countries.pop(0)
#countries.pop()
print(countries)
print(deleteCountry)

countries.remove('Morocco')

#sort and reverse

cars = ['bmw', 'honda', 'benz', 'tesla', 'rivian', 'toyota', 'maybach']
print(cars)
cars.sort()
print(cars)
cars.reverse()
print(cars)

'''

'''
evenNumbers = [4, 6, 8, 2, 20, 34, 12, 24, 70]

print(evenNumbers[1:-1:2])


for even in range(1, len(evenNumbers), 2):
    print(evenNumbers[even])
'''

for food in range(1, 10, 2):
    print(food)


