# it is a key value pair

myDict = {"a": "apple", "b": "ball", "c": "cat"}
print(myDict)
myDict2 = {"a": "apple", "b": "ball", "c": "cat", "rollNum": 12}
print(myDict2)
print("_____________retrieve or access the value using key______________")
print(myDict2["a"])
print(myDict.get("b"))
print("__________retreive all keys___________")
for i in myDict:
    print(i)
print("__________retreive all values___________")
for j in myDict:
    print(myDict[j])

print("__________retreive all values using values method___________")

for k in myDict.values():
    print(k)
print("values are ", myDict.values())

print("__________ check for values___________")
if "a" in myDict:
    print("key is present")
else:
    print("key is not present")
print("__________Length of dictionary__________")
print(len(myDict))
print("__________ adding___________")
myDict["d"] = "dog"
print(myDict)
print("__________ deleting __________")
myDict3 = {"rollnum1": "shabana", "rollnum2": "babjan", "rollnum3": "shan"}
print(myDict3)
myDict3.clear()
print(myDict3)
myDict4 = {"roll12": "sha", "roll13": "bab", "roll14": "ki"}
print(myDict4)
myDict4.pop("roll12")
# myDict4.pop("roll")
print(myDict4)
