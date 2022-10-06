names   = ["nisse", "stina", "bosse", "mimmi"]
animals = ["giraff", "myrslok", "tapir"]

def view(description, strings):
    index = 1
    for n in strings:
        print (f"{index}) {n}")
        index = index + 1

view("Lista med namn", names)
print()
view("Lista med djur", animals)