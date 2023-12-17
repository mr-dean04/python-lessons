'''
Write a code for a gym management system.
1. Ask the user what he wants to do (register & search)
2. Register a new member
3. Search for an existing member
4. Search for the database for location, body goals
5. For age, search for same age or less or greater than
'''
'''
print and input user choice
conditional statement for the user's choice
request 
'''

from register import *
from search import *
from gymMembers import *

shawerGymMembers = members

while True:
    print('********Shawers Gym, You are Welcome********')
    print('Select the options below\n\t1.Member Registration\t2.Search DataBase')
    userChoice = int(input())
    if userChoice == 1:
        shawerGymMembers.append(registerMember())
    elif userChoice == 2:
        search_user(shawerGymMembers)


