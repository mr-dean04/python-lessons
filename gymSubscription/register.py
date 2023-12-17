def registerMember():
    '''Register user details''' 
    print('Input your detail to get registered')
    print('What is your name ?')
    name = input()
    print('what is your age ?')
    age = int(input())
    print('Where do you live ?')
    location = input()
    print('What is your body goal (lean or bulk) ?')
    bodyGoal = input()
    userDetails = {
        'name': name.title(),
        'age' : age,
        'location' : location.title(),
        'bodyGoal' : bodyGoal.title()
    }
    print(userDetails)
    return userDetails