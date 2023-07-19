x = int(input("Enter your number:"))
def fizzbuzz(x):
    if x % 15 == 0:
        print("Fizzbuzz")
    elif x % 5 == 0 :
        print("Buzz")
    elif x % 3 == 0 :
        print("Fizz")
    else:
        print(x)
fizzbuzz(x)

