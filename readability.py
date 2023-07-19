text = input("Text: ")

def grade(l,s):
    yay = round(0.0588 * l - 0.296 * s - 15.8)
    if yay > 16:
        print("over 16")
    elif yay < 16:
        print("Grade 15")
    elif yay <15:
        print("Grade 14")
    elif yay <14:
        print("Grade 13")
    elif yay <13:
        print("Grade 12")
    elif yay <12:
        print("Grade 11")
    elif yay <11:
        print("Grade 10")
    elif yay <10:
        print("Grade 9")
    elif yay <9:
        print("Grade 8")
    elif yay <8:
        print("Grade 7")
    elif yay <7:
        print("Grade 6")
    elif yay <6:
        print("Grade 5")
    elif yay <5:
        print("Grade 4")
    elif yay <4:
        print("Grade 3")
    elif yay <3:
        print("Grade 2")
    elif yay <2:
        print("Grade 1")
    elif yay <1:
        print("Kindergarden")
    #use formula
    #print grade
def get_l(text):
    l = 0
    for char in text:
       if char.isalpha():
           l += 1
    l /= len(text.split)
   

    return l * 100
    #calculate average nu  mber of letters per sentence "
    # return l
def get_s(text):
    s = 0
    for char in text:
        if char == "." or char == "!" or char == "?":
            s += 1
        sl= len(text.split())
    #calculate average number of sentences per 100 words
    # return s


grade(get_l(text, get_s(text)))
