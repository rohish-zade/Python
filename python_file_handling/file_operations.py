# Assume we have the following file, located in the same folder as Python:
f = open("python_file_handling/demofile.txt", "r")
print(f.read())
f.close()


# Read Only Parts of the File
# By default the read() method returns the whole text, but you can also specify how many characters you want to return:
f = open("python_file_handling/demofile.txt", "r")
print(f.read(6))
f.close()


# Python code to illustrate with()
with open("python_file_handling/demofile.txt") as file:  
    data = file.read() 
print(data)


# Python code to illustrate split() function
with open("python_file_handling/demofile.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print (word)


# always close a file

# Write to an Existing File
# To write to an existing file, you must add a parameter to the open() function:
# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content

# Open the file "demofile.txt" and append content to the file:
f = open("python_file_handling/demofile.txt", "a")
f.write("\nWorking in MNC")
f.close()

#reading the file after the appending:
f = open("python_file_handling/demofile.txt", "r")
print(f.read())
f.close()


# Open the file overwrite the content:
f = open("python_file_handling/demofile.txt", "w")
f.write("The file is overwriten!")
f.close()

# #reading the file after the overwriting:
f = open("python_file_handling/demofile.txt", "r")
a = f.read()
print(a)


# Creating a New File
# To create a new file in Python, use the open() method, with one of the following parameters:
# "x" - Create - will create a file, returns an error if the file exist
# "a" - Append - will create a file if the specified file does not exist
# "w" - Write - will create a file if the specified file does not exist

# # Creating a file called "myfile.txt":
f = open("python_file_handling/myfile.txt", "x") #a new empty file is created!
f.close()

# Create a new file if it does not exist:
f = open("python_file_handling/myfile2.txt", "w")
f.close()

# Delete a File
# To delete a file, you must import the OS module, and run its os.remove() function:
import os
os.remove("python_file_handling/myfile.txt")

# Check if File exist:
# To avoid getting an error, you might want to check if the file exists before you try to delete it:


# Check if file exists, then delete it:
import os
if os.path.exists("python_file_handling/myfile.txt"):
    os.remove("python_file_handling/myfile.txt")
else:
    print("The file does not exist")
