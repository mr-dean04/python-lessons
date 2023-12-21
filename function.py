def greetings():
    print('Hello people')
    print('Hello good people')
    print('Bonjour bon ami')
    print('Ca va ?')

#greetings()

#Function takes parameter or agrument
def greetings_people(username):
    print('Hello ' + username)

#greetings_people('Mike')
#greetings_people('Johnson')

#positional agrument
def detail_people(name, age, location):
    print('Hello ' + name)
    print(name + ' is ' + str(age) + ' years old')
    print('You stay at ' + location)

#detail_people('Joe Mensah', 45, 'Takoradi')



def describe_friend(gender: str, name: str, age: int, location: str):
    print(name.title() + ' is your ' + gender + ' friend.')
    if gender == 'male' or gender == 'Male' or gender == 'M':
        print('He is ' + str(age) + ' years old')
    elif gender == 'female' or gender == 'Female' or gender == 'F':
        print('She is ' + str(age) + ' years old')
    print(name.title() + ' stays at ' + location)

#poistional argument
#describe_friend('M', 'kofi appiah', 34, 'Inchaban')

#keyword argument
#describe_friend(gender = 'Female', location = 'Essikado', name = 'ama mensah', age = 41)


def fullname(first_name, middle_name, last_name='Andoh'):
    print(first_name + ' ' + middle_name + ' ' + last_name)

#fullname('John', 'Kofi')

def full_name(first_name,  last_name, middle_name=''):
    print(first_name + ' ' + middle_name + ' ' + last_name)

#full_name('Esi', 'Johnson')

def fullName(first_name,  last_name, middle_name=''):
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name


getFullName = fullName(first_name= 'Sarah', middle_name = 'Maame Ama', last_name ='Johnson')
#print(getFullName)

def make_stew(dish, food_type, *ingredients):
    print('The number of dishes: ' + str(dish))
    print('Food type is ' + food_type)

    for ingredient in ingredients:
        print('-' + ingredient)
make_stew(6, 'potato_rice', 'tomatoes', 'oil', 'pepper', 'onion')
