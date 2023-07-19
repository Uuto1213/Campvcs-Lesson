h = int(input())
var =1
width = h

if h > 8:
    print("error")
elif h< 1:
    print("error") 
else:

    for i in range(h ):
        print(width*"", var*"#")
        width -= 1
        var +=1

    for i in range(h):
        print(width * " ", var * "#")
        print(" " * (h-i) + "#" * i)