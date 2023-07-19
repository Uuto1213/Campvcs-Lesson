x = int(input("Number 1"))
y = int(input("Number 2"))
print("What do you want to do?")
print("1. +")
print("2. -")
print("3. *")
print("4. /")
number = int(input())
if number == 1:
    print(x+y)
elif number == 2:
    print(x-y)
elif number == 3:
    print(x*y)
elif number == 4:
    print(x/y)
else:
    print("error, try again")
   
   