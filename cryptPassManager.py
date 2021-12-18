from cryptography.fernet import Fernet

'''Only need this function once. Multiple keys would be troublesome
def createKey():
    key = Fernet.generate_key()
    with open("key.key", "wb") as keyFile:
        keyFile.write(key)

Create key using function above        
createKey()'''

#Load Fernet key
def loadKey():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


#Initial password and key to gain access
masterPass = input("Please enter the master password:")
#Convert password to bytes(encode function instead of .bytes)
#  as the key is in byte format, then concatenate to key
key = loadKey() + masterPass.encode()
#Create variable for fernet w key for quick encoding/decoding
fer = Fernet(key)

#Create  main functions 
#---------------------------------------------------------
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data  = line.rstrip()
            user, passwd = data.split("|")
            print("User:", user, "| Password: ",
                fer.decrypt(passwd.encode()).decode())


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