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

users1 = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}
user1 = login(users1)
print(f"\nWelcome {user1}")

users2 = {"foo":"123", "bar":"hello", "foobar":"hello123"}
user2 = login(users2)
print(f"\nWelcome {user2}")