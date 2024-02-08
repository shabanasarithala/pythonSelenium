class Myclass:  # class
    a = "welcome to oops"

    def myFunction(self):  # method
        print("my function")

    def display(self, name):
        print(name)


obj = Myclass()  # objects
obj.myFunction()
obj.display("shabana")
print(obj.a)
