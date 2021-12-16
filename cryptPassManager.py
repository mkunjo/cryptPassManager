#Initial pass to gain access
masterPass = input("Please enter the master password:")

#Create functions 
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")
def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data  = line.rstrip()
            user, passwd = data.split("|")
            print("User:", user, ", Password: ", passwd)




while True:
    appMode = input("Would you like to add a new password(1) or view existing ones(2)? \nPlease enter 1 or 2. Enter 0 to quit.\n")
    if appMode == "0":
        break
    if appMode == "1":
        add()
    elif appMode == "2":
        view()
    else:
        print("Invalid selection.")
        continue