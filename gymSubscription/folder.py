import os

def delete_File():
    if ((os.path.exists(os.path.join(os.getcwd(), 'gymFolder', 'members.txt')))):
        os.unlink(os.path.join(os.getcwd(), 'gymFolder', 'members.txt'))
        os.rmdir(os.path.join(os.getcwd(), 'gymFolder'))

def append_members_file(member):
    if ((os.path.exists(os.path.join(os.getcwd(), 'gymFolder', 'members.txt')))):
        file = open (os.path.join(os.getcwd(), 'gymFolder', 'members.txt'), 'a')
        file.write(str(member) + '\n')
        file.close()
    else:
        os.makedirs(os.path.join(os.getcwd(), 'gymFolder'))
        file = open (os.path.join(os.getcwd(), 'gymFolder', 'members.txt'), 'a')
        file.write(str(member) + '\n')
        file.close()