import pickle

# Pickle is used to store data in a file
# The data can be retrieved later
# The data can be of any type

def open_and_store(data, filename):
    # Open the file
    file = open(filename, 'wb')

    # Store the data
    pickle.dump(data, file)

    # Close the file
    file.close()

def open_and_retrieve(filename):
    file=open(filename,'rb')
    data=pickle.load(file)
    file.close()
    return data

#Example data to binarize
data = [
    {'Name': 'John', 'Age': 28, 'Phone': 1234567890},
    {'Name': 'Alice', 'Age': 22, 'Phone': 9876543210},
    {'Name': 'Bob', 'Age': 32, 'Phone': 1231231230}
]

#Binarize and store the data
open_and_store(data,'data.bin')

#Retrieve the data
data=open_and_retrieve('data.bin')
print(data)