import re


def check_login(login):
    if len(login) < 6:
        return False
    if not re.match("^[a-zA-Z0-9_]*$", login):
        return False
    return True

def check_password(password, username):
    if len(password) < 8:
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if username in password or password in username:
        return False  
    if not re.search("[!@#$%^&*()_+=-]", password):
        return False  
    return True

print ("Let's Sign up!")
print ()
print ("""Your login should be:
At least 6 characters long 
Only letters, numbers, and underscores""")
print ()
print ("""Your Password should contain:
8 characters
One uppercase letter
One lowercase letter
One number
One special character
""")
print ("The password should not contain the username or parts of the username")
print ()
while True:
    username = input("Enter your login: ")
    password = input("Enter your password: ")

    if check_login(username) and check_password(password, username):
        print("Welcome! Your login and password are strong.")
        break
    else:
        print("Login and password are weak. Please enter a new login and password.")
