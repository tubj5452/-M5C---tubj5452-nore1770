options = {"r":"Try again", "q":"Quit"} 
users = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}

def menu(prompt, options):
    for n in options:
        print (f"\t{n}) {options[n]}")
    
    enter = True
    while enter:
        searched = input(f"{prompt}")
        if searched in options.keys():
            return searched    

def login(users):
    enter = True
    while enter:
        user = input("User: ")
        password = input("Password: ")
        if user in users.keys() and password in users[user]:
            return user 
            enter = False
        else:
            print ("\nInvalid username or password\n")   
            if menu("\nOption: ", options) == "q":
                break
            
user = login(users)

