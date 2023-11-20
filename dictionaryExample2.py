'''
A program that request for the user's:
1. name 
2. age
3. salary expectation
4. id
5. location
'''

employee = {} #empty dictionary

print('What is your name ?')
name = input()

print('what is your age ?')
age = int(input())

print('what is your salary expectation ?')
salaryExpectation = int(input())

print('what is your ID ?')
id = input()

print ('where do you stay ?')
location = input()

employee['employeeName'] = name
employee['employeeAge'] = age
employee['employeeSalary'] = salaryExpectation
employee['employeeID'] = id
employee['place of stay'] = location

print(employee)