greeting = input("Greeting: ")

def  bank(string):
    if greeting[:5].lower() == "hello":
        print("$0")
    elif greeting[0].lower() == "h":
        print("$20")

    else:
        print("Pay $100!")

bank(greeting)

    # if greeting[0] == "h" and greeting[1] == "e" and greeting[2] == "l" and greeting[3] == "l" and greeting[4] == "o":