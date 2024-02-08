# we have to represent list with in [] square bracket
# List is a collection which is in ordered and mutable and is represented by square bracket []
mylist = ['a', 'b', 'c']
print(mylist)
myNumList = [1, 2, 3, 4]
print(myNumList)
mylist2 = list()
print(mylist2)
mylistMixed = ['s', 22, "Bab", 28]
print(mylistMixed)
# access the items from list , Index starts with 0
print(mylistMixed[2])
print(mylistMixed[-1])
# print(mylistMixed[-5])
# print(mylistMixed[6])

fruits = ["apple", "grapes", "banana", "orange", "mangoes"]
print(fruits)
print(fruits[1:5])
print(fruits[1:7])

# change the item of list
fruits[1] = "custard"  # grapes replaced with custard
print(fruits)

print("_______printing the list using for loop__________")
for i in fruits:
    print(i)
print("_________ check if the item is present in list or not______________")
for i in fruits:
    if i == "orange":
        print(i)

print("_______printing in range using for loop__________")
for i in fruits[2:4]:
    print(i)

print("_________ check if the item is present in list or not______________")
if "apple" in fruits:
    print("yes")
else:
    print("No")

print("___________ length or size of fruits___________")
print("Length of the fruits list is ", len(fruits))

print("____________inserting into the list_____________________")
fruits.insert(3, "Jamun")
print(fruits)
print("_____________ appending to list , this will automatically append at last____________________")
fruits.append("jack")
print(fruits)
print("____________remove item from list_____________________")
fruits.pop(1)
print(fruits)
print("_____________clear the list____________________")
animalList = ["lion", "elephant"]
print(animalList)
animalList.clear()
print(animalList)
print("_____________copy the list____________________")
NewFruitsList = fruits.copy()
print(NewFruitsList)
print("_____________ combine the list____________________")
FinalFruitsList = NewFruitsList + fruits
print(FinalFruitsList)
print("_____________ compare the list____________________")
charList1 = ['a', 'b', 'c']
charList2 = ['a', 'c', 'b']
if charList1 == charList2:
    print("lists are equal")
else:
    print("lists are not equal")
