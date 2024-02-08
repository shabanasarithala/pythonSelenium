class MyObject:
    def firstMethod(self):
        print("This is in first method")

# we can create multiple objects for the same class
obj1 = MyObject()
obj1.firstMethod()

obj2 = MyObject()
obj2.firstMethod()
