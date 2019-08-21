import hashlib
d={}

def makeAccount():
    username = input("Create a username: ")
    password = input("Create a password: ")
    hashPass = hashlib.md5(password.encode()).hexdigest() 
    d[username] = hashPass
    print("Congratulations! You have now made an account with the following username: " + username)

makeAccount()

user_input = input("Do you want to make another account? ")
while user_input == "yes":
    makeAccount()
    user_input = input("Do you want to make another account? ")
    

print("Sign in. ")
sign_in_user = input("What is your username? ")
while sign_in_user not in d:
    sign_in_user = input("Username not found. Try again. ")
sign_in_pass = input("What is your password? ")
        
hash_sign_in_pass = hashlib.md5(sign_in_pass.encode()).hexdigest()

if d[sign_in_user] == hash_sign_in_pass:
    print("You have now signed in.")
else:
    while d[sign_in_user] != hash_sign_in_pass:
        sign_in_pass = input("Wrong password. Try again. ")
        hash_sign_in_pass = hashlib.md5(sign_in_pass.encode()).hexdigest()
    print("You have now signed in.")

logOut = input("Do you want to log out? ")
if logOut == "yes":
    print("Goodbye!")
else:
    print("You are still signed in.")
    
