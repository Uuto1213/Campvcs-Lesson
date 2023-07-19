# def hello(obj):
#     print("hello" + obj)
# hello("matthew")
# name = "scott"
# hello(name)

# def sum(x,y):
#     return(x+y)

# def even(x):
#     if x% 2 == 0:
#         return True
#     else:
#         return False
    
# def inrange(n,a,b):
#     if n>=a and n<=b:
#         return True
#     else:
#         return False
# print(inrange(0,-5,5))
# print(inrange(10,20,30)

# def Olivia(name):
#     def uchan(str):
#         if str == "Uchan":
#             return True
#     if uchan(name):
#         print("Uchan Bale")
# Olivia("rex")

def fac(x):
    if x == 1:
        return 1
    else:
        return x * fac(x-1)

fac(5)
print(fac(5))