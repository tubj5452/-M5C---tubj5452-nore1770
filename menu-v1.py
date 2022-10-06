options = {"a":"Add item", "l":"List items", "q":"Log out"}

def view(description, strings):
    print(f"{description}")
    for n in strings:
        print (f"\t{n}) {strings[n]}")

def search(prompt, strings):
    enter = True
    while enter: 
        searched = input(f"{prompt}")
        if searched in strings.keys():
            print (f"\nYou selected option {searched}): {strings[searched]}")
            enter = False
  
view("Select an action:\n", options)
search("Option: ", options)