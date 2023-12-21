def search_user(membersDetail):
    print('Search by\n\t1. Name  2. Age  3. Location  4. BodyGoal')
    userSearchChoice = int(input())

    if (userSearchChoice == 1):
        print('Enter your user name')
        searchName = input()
        for userDetail in membersDetail:
            if searchName.title() == userDetail['name']:
                print(searchName.title() + ' is already register')
                print('Below are the details:')
                print(userDetail)

    if (userSearchChoice == 2):
        print('Enter age of member')
        searchAge = int(input())
        print('Search for age\n1. Equal to ' + str(searchAge) + '  2. Less than ' + str(searchAge) + '  3. Greater than ' + str(searchAge))
        ageIndex = int(input())
        printOnce = True
        if ageIndex == 1:
            for userDetail in membersDetail:
                if searchAge == userDetail['age']:
                    if printOnce == True: #same as -> if printOnce
                        printOnce = False
                        print('Member found!')
                        print('Below are the details:')
                    print(userDetail)
        elif ageIndex == 2:
            for userDetail in membersDetail:
                if searchAge > userDetail['age']:
                    if printOnce:
                        printOnce = False
                        print('Member found!')
                        print('Below are the details:')
                    print(userDetail)
        elif ageIndex == 3:
            for userDetail in membersDetail:
                if searchAge < userDetail['age']:
                    if printOnce:
                        printOnce = False
                        print('Member found!')
                        print('Below are the details:')
                    print(userDetail)
        printOnce = True            
    if (userSearchChoice == 3):
        print('Enter user\'s location')
        searchLocation = input()
        for userDetail in membersDetail:
            if searchLocation.title() == userDetail['location']:
                print(searchLocation.title()+ ' members' + ' found!')
                print('Below are the details:')
                print(userDetail)

    if (userSearchChoice == 4):#i need to create a conditional statement so user can choose either lean or bulk. 
        print('Enter \'Lean, lean,\' or \'Bulk, bulk\' for the search')
        searchBodyGoal = input()
        if searchBodyGoal == 'Lean' or 'lean':
            for userDetail in membersDetail:
                if searchBodyGoal.title() == userDetail['bodyGoals']:
                    print('For' + ' ' + searchBodyGoal.title() + ',' + ' ' + 'here are the search results:')
                    print(userDetail)
        elif searchBodyGoal == 'Bulk' or 'bulk':
            for userDetail in membersDetail:
                if searchBodyGoal.title() == userDetail['bodyGoals']:
                    print('For' + ' ' + searchBodyGoal.title() + ',' + ' ' + 'here are the search results:')
                    print(userDetail)#no help from A.I.....😅
        
   
