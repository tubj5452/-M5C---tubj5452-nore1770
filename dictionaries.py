users = {"nisse":"apa", "bosse":"ko", "stina":"t-rex"}
data = {"nisse":["luva", "vante"], "bosse":["spik", "skruv", "hammare"], "stina":["tidsmaskin"]}

def view(description, strings):
    print(f"{description}")
    for n in strings:
        print (f"\t{n}) {strings[n]}")

def search(prompt, strings):
    searched = input(f"{prompt}")
    
    enter = False
    for n in strings:
        if n == searched:
            print (f"\nData lagrat för {n}: {strings[n]}")
            enter = True
    if enter == False:
        print(f"\nAnvändaren {searched} finns inte")

print ("Användare:\n")
for n in users:
    print (f"\t{n}")

view("\nAnvändare och lösenord:\n", users)
view("\nAnvändare och deras data:\n", data)
search("\nSlå upp användare: ", data)