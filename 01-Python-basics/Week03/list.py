# Lists are ordered and changeable

fruits = ["apple", "banana", "cherry", "banana"]

print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[3])

print("------------------")

# # change item value
# fruits[0] = "kiwi"
# print("new fruits list:", fruits)


# # Append item to the list
# fruits.append("orange")
# print("after append:", fruits)

# # Remove item from the list
# fruits.remove("banana") # it only removes the first appearance of the item
# print("after remove:", fruits)

# # So, if you want to remove all appearances of an item, you can use a loop
# while "banana" in fruits:
#     fruits.remove("banana")
# print("after removing all bananas:", fruits)