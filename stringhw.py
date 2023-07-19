
str = input("Sting:")
for i in range(len(str)):
    if i % 2 == 1:
        print(str[i], end = "")

print(st[0], end = "")
for i in st[1:]:
    if i == st[0]:
        print("*", end = "")
    else:
        print(i,end="")