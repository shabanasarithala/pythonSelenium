i, j = 4, 5  # global level variables


class Variables:
    a, b = 1, 2  # class level variables
    print(a, b)

    def addition(self):
        print(self.a + self.b)
        print(i + j)

    def additionNew(self, x, y): # local variables or method level
        print(x + y)


obj = Variables()
obj.addition()
obj.additionNew(55,35)
print(i,j)
