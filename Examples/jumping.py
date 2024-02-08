for i in range(1,10):
    if i==4:
        break
    print(i)

print("-----------------")

for i in range(1,10):
    if i==2 or i==4 or i==8:
        continue
    print(i)