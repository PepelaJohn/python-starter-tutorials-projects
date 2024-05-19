# from cryprography.fernet import Fernet 
pwd = input("What it the master password")
'''
def write_key():
    key  = Fernet.generatekey()
    with open('key.key', "wb") as key_file:
        key_file.write(key)'''
'''
def load_key():
    key  = Fernet.generatekey()
    with open('key.key', "wb") as key_file:
        key_file.read(key)
        return key
        '''






def view():
    mpwd = input("What is your master password? ")
    if mpwd != pwd:
        print("Wrong password")
    else:
        with open('pwd', 'r')as f:

             for line in f.readlines():
                text = line.rstrip()
                print("Name: ",text.split("|")[0])
                print("PassWord: ",text.split("|")[1])  
    
def add():
    name = input('What is your name: ')
    passw = input('What is your password')

    with open('pwd', 'a') as f:
        f.write(name + "|"+ passw + "\n")

while True:
    mode = input("Would you like to add a new password or view the existing ones (view/add)")

    if mode == 'view':
        view()
    if mode == 'add':
        add()
    else:
        quit()

