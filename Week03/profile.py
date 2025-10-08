import json

def save_data(data):
    with open("profile.json", "w") as f:
        json.dump(data, f)

def load_data():
    with open("profile.json", "r") as f:
        return json.load(f)

# Get age with validation
while True:
    try:
        age = int(input("Age: "))
        break  # Exit loop if conversion is successful
    except ValueError:
        print("Please enter a valid number for age!")

profile = {
    "name": input("Name: "),
    "age": age,
    "skills": input("Enter skills separated by commas: ").split(",")
}

save_data(profile)
print("Data saved!\n")
print("Loaded data:", load_data())
