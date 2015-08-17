import os.path

while True:
    filepath = Ask for a file path until a valid file is given

fileHandler = open(filepath)
content = Read full content of the file

print("The file's content is:")
print(content)

Rewind the cursor to the beginning of the file

lines = Read the file and return a list of lines (each line is an element of the list)
print("The file's lines are:")
print(lines)

# Close the file!
fileHandler.close()