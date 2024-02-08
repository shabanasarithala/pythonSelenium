# methods
# mutable - can change
# string is immutable
a= 'python'
b='python'

print(a,b)
print(id(a))
print(id(b))

str1 = a+"welcome"
print(id(a))

# slicing
str = "welcome"
print(str[1:3])
str1 = "shabana"
print(str1)
print(str1[1:-2])

# ord() - converts char to ascii
# chr() - ascii to char
print(ord('A'))
print(chr(65))

# max , min, length
print(max("abcd"))
print(min("abcd"))
print(len("123456"))

print("come" in str) # True
print("do" in str) # Flase
print("do" not in str) # True

