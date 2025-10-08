# To read / write into a file

# Read from a file
with open("notes.txt", "r") as f:
    content = f.read()
    print(content)

# Write to a file
with open("notes.txt", "w") as f:
    f.write("Hello, Python!\n")  # will clear exisiting content and write new content

# Read from a file
with open("notes.txt", "r") as f:
    content = f.read()
    print(content)