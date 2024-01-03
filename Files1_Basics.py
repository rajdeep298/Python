# open the file in read mode
fp = open("Input.txt", "r")

# Read the file
print(fp.read())

# Close the file
fp.close()

# open the file in write mode
fp = open("Input.txt", "w")
fp.write("Hello World")
fp.close()

# open the file in append mode
fp = open("Input.txt", "a")
fp.write("Hello World")
fp.close()

# open the file in r+ mode
fp = open("Input.txt", "r+")
fp.write("Hello World")
fp.close()

# open the file in w+ mode
fp = open("Input.txt", "w+")
fp.write("Hello World")
fp.close()

# open the file in a+ mode
fp = open("Input.txt", "a+")
fp.write("Hello World")
fp.close()

# open the file in rb mode
fp = open("Input.txt", "rb")
print(fp.read())
fp.close()

# open the file in wb mode
fp = open("Input.txt", "wb")
fp.write("Hello World")
fp.close()

# with open
with open("Input.txt", "r") as fp:
    print(fp.read())
    fp.close()

# readlines
with open("Input.txt", "r") as fp:
    print(fp.readlines())
    fp.close()

# writelines
with open("Input.txt", "w") as fp:
    fp.writelines(["Hello World", "Hello World"])
    fp.close()

# seek
with open("Input.txt", "r") as fp:
    fp.seek(5)  # move the cursor to 5th position
    print(fp.read())
    fp.close()
