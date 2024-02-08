name = "shabana"
print(name.isdigit()) # false
print(name.isupper()) #false
print(name.islower()) #true
print("WEL".isupper()) #true
print("SWwe".isupper()) # false
print("SWwe".islower()) #false
print("WED".lower())
print("cfe".upper())

s = "welcome to python training"
print(s.endswith("ing")) # true
print(s.startswith("wel")) # true
s2 = s.replace("to","in")
print(s2)

s3 = "WELCOME"
s4 = "welcome"
print(s3==s4) # false
print(s3.split("L"))
