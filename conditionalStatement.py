
'''
age = 10  #assignment

if age == 20: #comparison 
    print('You are 24 years old')

elif age == 25:
    print('Indeed you are 25')

elif age == 30 or age == 50:
    print('You are 30 years old')

else:
    print('I dont know your age')


number = 10

if number <= 10:
    print('Number is above 10')
'''

names = ['john', 'peter', 'maxwell', 'joseph', 'joe']
numbers = [4, 6, 2, 3, 1, 8, 4, 2]

checkNumber = 2
checkName = 'john'

if checkName or 'kweku' in names[:]:
    print('John is present')

if checkNumber in numbers:
    print('2 is present')

