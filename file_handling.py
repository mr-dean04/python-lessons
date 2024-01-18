import os
'''
#os.path.join('C', 'Users', 'Desktop')
os.makedirs()

for object in os.listdir(os.getcwd()):
    if os.path.isfile(object):
        print(object)


print([object for object in os.listdir(os.getcwd()) if os.path.isfile(object)])

os.path.exists('path')

'''

if (os.path.exists(os.path.join(os.getcwd(),'folder'))) == False:
    os.makedirs(os.path.join(os.getcwd(),'folder'))

with open(os.path.join(os.getcwd(),'folder', 'data.txt'), 'w') as writeFile:
    writeFile.write('Hello world')


with open(os.path.join(os.getcwd(),'folder', 'data.txt'), 'r') as readFile:
    info = readFile.read()
    print(info)
