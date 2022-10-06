def add (prompt, strings):
    strings.append(input(f"{prompt}"))
    return strings


# Test of the function add with the list ducks.

ducks = ["Huey", "Dewey", "Louie"]

print(f"Ducks: {ducks}\n")

ducks_alias = add("\tAdd a duck: ", ducks)

print(f"\n\t Ducks: {ducks}")
print(f"Alias of Ducks: {ducks_alias}\n")

# Test of the function add with the list composers.

composers = ["Mozart", "Bach"]

print(f"\nComposers: {composers}\n")
add("\tAdd a composer: ", composers)

print(f"\nComposers: {composers}")