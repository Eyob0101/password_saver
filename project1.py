def show():
    with open('password_storage.txt', 'r') as f:
        for line in f.readlines():
            print(line)

def add():
    name = input("account user name: ")
    pwd = input("password for account: ")
    acc_for = input("account for: ")

    with open('password_storage.txt', 'a') as f:
        f.write('user name :' + name + ", password :" + pwd + ", account for :" + acc_for + "\n")

while True:
    option = input(""" 
            Menu
    - To add a user name and password type (add)
    - To view existing user name and password type (show)
    - To quit from the page type (quit)
    >>> """)

    if option == "quit":
        break
    
    if option == "show":
        show()

    elif option == "add":
        add()

