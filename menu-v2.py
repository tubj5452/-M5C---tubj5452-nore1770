def menu(title, prompt, options):
    print(f"{title}\n")
    for n in options:
        print (f"\t{n}) {options[n]}")
        
    enter = True
    while enter:
        searched = input(f"{prompt}")
        if searched in options.keys():
            return searched
    
options1 = {"a":"Add item", "l":"List items", "q":"Log out"}
opt1 = menu("Select an action", "Action: ", options1)
print(f"\nYou selected action {opt1}) {options1[opt1]}\n")

options2 = {"r":"Try again", "q":"Quit"}
opt2 = menu("What do you want to do?", "My choice: ", options2)
print(f"\nYou selected option {opt2}) {options2[opt2]}")


