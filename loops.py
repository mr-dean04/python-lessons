'''
rangeNumber = list(range(1, 10, 2))
print(rangeNumber)


numbers = [3, 5, 1, 2, 4, 7, 8, 2, 3, 5, 4]

for number in numbers:
    print(number)

for book in range(len(numbers)):
    print(numbers[book])


coordinate = [[2, 3], [4, 6], [4, 3], [4, 5], [4, 1]]

if 3 <= coordinate[1][1]:
    print('the number is 6')
'''

odd_numbers = {
    'number_1' : 'one',
    'number_2' : 'three',
    'number_3' : 'five',
    'number_4' : 'seven',
    'number_5' : 'nine',
    'number_6' : 'eleven'
}

#print(odd_numbers)

'''
odd_numbers.items()
odd_numbers.keys()
odd_numbers.values()
'''

'''
for keys, values in odd_numbers.items():
    
    print(keys, ": " + values)
'''

'''    
for values in odd_numbers.keys():
    if 'number_1' == values:
        print('The number 1 included')
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
    },
    'user3' :{
    'name' : 'Shawers',
    'age' : 150,
    'location' : 'Essikadi',
    'bodyGoals' : 'lean'
    }
}

count_number = 0

'''
for items_keys, items_values in shawersGym.items():
    for items_age in items_values.items():
        if items_age[0] == 'age':
            if items_age[1] > 20:
                count_number+=1
'''

for items_keys, items_values in shawersGym.items():
    if items_values['age'] > 20:
        count_number +=1

print(count_number)
             







