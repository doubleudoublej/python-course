# Tuples are immutable lists -->  cannot be changed after creation

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print("-------------------")
print(my_tuple[0])

my_tuple[0] = 10  # will raise an error