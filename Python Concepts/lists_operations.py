# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

myList = [1, 3, 4, 5, 2, 6, 7, 8, 9]

print('Original List:',myList)
print('Original List:',myList[0])
print('Element at 2nd Index position:',myList[2])
print('Elements from 0th Index to 4th Index:',myList[0: 5])
print('Element at -7th Index:',myList[-7])

#To append an element to a list
myList.append(10)
print('Append:',myList)

#To find the index of a particular element
print('Index of element \'6\':',myList.index(10)) #returns index of element '6'

#To sort the list
myList.sort()

#To pop last element
print('Poped Element:',myList.pop())

print('After pop and sort List:',myList)


#To remove a particular element from the lsit BY NAME
myList.remove(6)
print('After removing \'6\':',myList)

#To insert an element at a specified Index
myList.insert(5, 6)
print('Inserting \'6\' at 5th index:',myList)

#To count number of occurences of a element in the list
print('No of Occurences of \'1\':',myList.count(1))

#To extend a list that is insert multiple elemets at once at the end of the list
myList.extend([11,0])
print('Extending list:',myList)

#To reverse a list
myList.reverse()
print('Reversed list:',myList)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print(thislist[0:4])
print(thislist[2:])
print(thislist[-4:-1])


thislist2 = ["apple", "banana", "cherry"]
thislist2[1] = "blackcurrant"
print(thislist2)


thislist3 = ["apple", "banana", "cherry"]
for x in thislist3:
  print(x)

thislist4 = ["apple", "banana", "cherry"]
if "apple" in thislist4:
  print("Yes, 'apple' is in the fruits list")

thislist5 = ["apple", "banana", "cherry"]
print(len(thislist5))


thislist6 = ["apple", "banana", "cherry"]
thislist6.insert(1, "orange")
print(thislist6)


thislist = ["apple", "banana", "cherry"]

thislist.clear()
print(thislist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)