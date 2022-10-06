strings = []
#s = input("Mata in antal strängar du vill ha i din lista: \n")
#n = int(s)
n = 5 

def add(prompt, strings):
    strings.append(input(f"{prompt}"))
    return strings

def view(description, strings):
    print(f"{description}")
    index = 1
    for i in strings:
        print (f"{index}) {i}")
        index += 1

print(f"n = {n}")

for i in range (n):
    add("\nLägg till en sträng: ", strings)

view(f"\nDu har matat in följande {n} strängar\n", strings)
