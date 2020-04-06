import array

# initializing array
arr = array.array('i', [1, 2, 3, 1, 5])     # initialize array with integers ('i')

# printing original array
print ("The new created array is : ",end="")
for i in range (0, 5):
    print (arr[i], end=" ")

# using append() to insert new value at end
arr.append(6);

# printing appended array
print ("\nThe appended array is : ", end="")
for i in range (0, 6):
    print (arr[i], end=" ")

print("\n")

# using insert() to insert value at specific position
# inserts 5 at 2nd position
arr.insert(2, 5)

# printing array after insertion
print ("\nThe array after insertion is : ", end="")
for i in range (0, 7):
    print (arr[i], end=" ")

print("\n")

arr.remove(1)

# deleting a  value from array
print ("\nThe array after deletion is : ", end="")
for i in range (0, 6):
    print (arr[i], end=" ")

print("\n")