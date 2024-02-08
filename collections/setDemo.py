myfruitsset = {"apple", "banana", "orange"}
print(myfruitsset)
# print(myfruitsset[0])
print("___________________________")
for i in myfruitsset:
    print(i)

print("_________ adding single item to set______________")
myfruitsset.add("grapes")
print(myfruitsset)
print("_________ adding multiple items to set______________")
# myfruitsset.update('a','b','c',2,3)
myfruitsset.update("a", "b", "c")
print(myfruitsset)
print("_________ length of set______________")
print(len(myfruitsset))
print("_________ remove item from set______________")
myfruitsset.remove("a")
print(myfruitsset)
print("_________ combining sets using union______________")
set1 = {"x", "y", "z"}
set2 = {"d", "e", "f"}
set3 = set1.union(set2)
print(set3)
print("_________ combining sets using update_____________")
set4 = {"1", "2", "3"}
set5 = {"1", "2", "3", "4"}
set4.update(set5)
print(set4)
print("___________ example of pop method________________")
setExample = {"200", "300", "400", "500"}
setExample.pop()
print(setExample)
