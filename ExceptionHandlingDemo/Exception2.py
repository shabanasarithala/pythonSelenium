print("started execution")
try:
    print(10 / 5)
    print(10 / 0)  # ZeroDivisionError exception
except ZeroDivisionError:
    print("Exception handled")
finally:
    print("I am always there...")

print("completed execution")
