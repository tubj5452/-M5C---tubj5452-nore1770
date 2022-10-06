users = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}

def login(users):
    enter = True
    while enter:
        user = input("User: ")
        password = input("Password: ")
        if user in users.keys() and password in users.values():
            print(f"\nWelcome {user}\n")
            enter = False
        else:
            print ("\nInvalid username or password\n")

login(users)
 
