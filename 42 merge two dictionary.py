# proram that merge two dictionary
print("😍 ------------------------- 😍")
# method 1   (by bar '|' )
dictionary_1 = {"jonh":89,"lisa":32}
dictionary_2 = {"peter":49,"lisa":62}

print(dictionary_1 | dictionary_2)


# method 2   (by quark '**' )

print({**dictionary_1, **dictionary_2})

# method 3  ( by using copy()  and update() method)


dictionary_3 = dictionary_2.copy()
dictionary_3.update(dictionary_1)

print(dictionary_3)