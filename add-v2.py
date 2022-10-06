def add(prompt, strings):
    strings.append(input(f"{prompt}"))
    return strings

# Test of the function add with the list ducks.

ducks = ["Huey", "Dewey", "Louie"]

print(f"Ducks: {ducks}\n")

add("Add a duck: ", ducks)
print(f"\nDucks: {ducks}\n")

add("Add a duck: ", ducks)
print(f"\nDucks: {ducks}\n")

# Test of the function add with the list composers.

composers = ["Mozart", "Bach"]
print(f"Composers: {composers}\n")

add("Add a composer: ", composers)
print(f"\nComposers: {composers}\n")