def add(number1: int, number2:int):
    totalNumber = number1 + number2
    return totalNumber


def sub(number1: int, number2:int):
    totalNumber = number1 - number2
    return totalNumber

def mult(number1: int, number2:int):
    totalNumber = number1 * number2
    return totalNumber

userResponse = 'start'

while (userResponse != 'quit'):
    
    print('Select what you want to do\n1. Add\t2.Sub\t3.Mult')
    userChoice = int(input())

    print('Enter your first number')
    numberOne = int(input())

    print('enter your second number')
    numberTwo = int(input())

    if userChoice == 1:
        recvTotal = add(numberOne, numberTwo)
        print('Your total addition is ' + str(recvTotal))

    elif userChoice == 2:
        recvTotal = sub(numberOne, numberTwo)
        print('Your final value is ' + str(recvTotal))

    elif userChoice == 3:
        recvTotal = mult(numberOne, numberTwo)
        print('Your final multiplied is '+ str(recvTotal))

    else:
        print('Invalid input try again')


    print('Type quit to end the calculation')
    userResponse = input()
