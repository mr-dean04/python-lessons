#Dictionary

'''
fruits = ['manago', 'banana', 'apple', 'pineapple']

employee = {
    'name': 'Maxwell Appiah',
    'age': 45,
    'id': '4154AD',
    'salary': 50000
}

#print(employee)

#print value of the key
print(employee['name'])
print(employee['age'])

#modify values of the key
employee['name'] = 'Kojo Bones'
employee['salary'] = 41000

#append new key and value
employee['location'] = 'Sekondi'

#find insert after any specific key

#delete a key-value pair
del employee['age']
print(employee)

foodstuffs = {
    'name' : "Dean's kitchen",
    'fruits' : ['pawpaw', 'mango', 'apple', 'orange'],
    'vegetables' : ['tomato', 'carrot', 'onion'],
    'spices' : ['onga', 'rosemary', 'maggi', 'remi']
}

print(foodstuffs['fruits'])
print(foodstuffs['fruits'][0])

foodstuffs['fruits'][0] = 'guava'
print(foodstuffs['fruits'])

foodstuffs['fruits'].append('coconut')
print(foodstuffs['fruits'])

'''

shawersGym = {
    'user1' : {
        'name': 'Kofi Bones',
        'age' : 29,
        'location' : 'Sekondi',
        'bodyGoals' : 'bulk'
    },
    'user2' :{
        'name' : 'Enjoy',
        'age'  : 100,
        'location' : 'Essikado',
        'bodyGoals' : 'lean'
    }
}

#print(shawersGym)

newMember = {
    'name' : 'Shawers',
    'age' : 150,
    'location' : 'Essikadi',
    'bodyGoals' : 'lean'
}

#append a new member (dictionary) to shawers gym
shawersGym['user3'] = newMember

print(shawersGym)
print(shawersGym['user3']['name'])
