def add (prompt, strings):
    strings.append(input(f"{prompt}"))
    return strings


# Test of the function add with the list ducks.

ducks = ["Huey", "Dewey", "Louie"]

print(f"         Ducks: {ducks}")
print()

ducks_alias = add("    Add a duck: ", ducks)

print(f"\n         Ducks: {ducks}")
print(f"Alias of Ducks: {ducks_alias}")
print()

# Test of the function add with the list composers.

composers = ["Mozart", "Bach"]
print(f"\n     Composers: {composers}")
print()

add("Add a composer: ", composers)

print(f"     Composers: {composers}")
print()