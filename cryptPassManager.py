#Initial pass to gain access
masterPass = input("Please enter the master password:")

#Create functions 
def view():
    pass

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd)


while True:
    appMode = input("Please enter 1 or 2. \nWould you like to add a new password(1) or view existing ones(2)? \nEnter 0 to quit.\n")
    if appMode == "0":
        break
    if appMode == "1":
        add()
    elif appMode == "2":
        pass
    else:
        print("Invalid selection.")
        continue