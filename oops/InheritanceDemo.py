class A:
    def method1(self):
        print("this is method1 of class A")

    def method2(self):
        print("this is method2 of class A")


class B(A):  # here we are inheriting class A into class B by keeping class A in parentheses of class B.
    # Here class A is parent and B is child.
    def method3(self):
        print("this is from method3 of class B")


obj_B = B()
obj_B.method3()
obj_B.method1()
# objective of inheritance is to avoid duplicate and code re-usability
