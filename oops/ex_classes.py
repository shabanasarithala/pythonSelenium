class MyClass:
    def myMethod(self):  # instance method
        print("This is my method")

    @staticmethod
    def myStaticMethod(message):  # static method, can be created using @staticmethod annotation
        print(message, "I am in static method")


obj = MyClass()  # creating object of myclass
obj.myMethod()
MyClass.myStaticMethod("Hello ")
