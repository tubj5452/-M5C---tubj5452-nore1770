names   = ["nisse", "stina", "bosse", "mimmi"]
animals = ["giraff", "myrslok", "tapir"]

def view(description, strings):
    print(f"\n{description}\n")
    index = 0
    for n in strings:
        index += 1
        print (f"{index}) {n}")

view("Lista med namn", names)

view("Lista med djur", animals)



