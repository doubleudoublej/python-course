# side by side comparison of Python dictionary and JSON format


'''
# Python dictionary
student = {"name": "Jay", "age": 22, "skills": ["Python", "Flask"]}


JSON format example:
{
  "name": "Jay",
  "age": 22,
  "skills": ["Python", "Flask"]
}
'''


import json

student = {"name": "Jay", "age": 22, "skills": ["Python", "Flask"]}

# Load from JSON file
with open("data.json", "r") as f:
    loaded = json.load(f)

print(loaded)
print("--------------------")

# Save to JSON file
with open("data.json", "w") as f:
    json.dump(student, f)

# Load from JSON file
with open("data.json", "r") as f:
    loaded = json.load(f)

print(loaded)