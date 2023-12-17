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
