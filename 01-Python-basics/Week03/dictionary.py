# Dictionaries are unordered and changeable

student = {
    "name": "Jia Jun",
    "Year": "4",
    "gender": "M",
}

print(student)
print("-------------------")

# # Dictionaries can be added or modified

# student["email"] = "email@e.ntu.edu.sg"     # add new key
# student["Year"] = "Final Year"             # update existing key
# print(student)
# print("-------------------")

# # Deleting keys

# del student["gender"]
# print(student)
# print("-------------------")

# # Alternative way to delete keys using ".pop()"
# student.pop("Year")
# print(student)
# print("-------------------")




# # Dictionary inside a Dictionary

# students = {
#     "Jia Jun": {
#         "Year": "4",
#         "gender": "M"
#     },
#     "Karin":{
#         "Year": "1",
#         "gender": "F"
#     },
#     "Eklavya":{
#         "Year": "1",
#         "gender": "M"
#     }
# }

# print(students)
# print("--------------------")
# print(students["Karin"]["gender"])  
# print("-------------------") 



# # List inside Dictionary

# me = {
#     "name": "Jay",
#     "age": 26,
#     "skills": ["Python", "HTML", "Flask"]
# }

# print(me)
# print("-------------------")
# print(me["skills"][2])
# print("-------------------")
# print(me["name"],"knows", me["skills"][0])   
# print("-------------------")



