q = 25
p = 10
n = 5
c1 = 1
coins = 0

while True:
    print("How much cash do you have?")
    c = float(input(""))
    c = round(c*100)
    if c > 0:
        break
     
while c >= q:
    c = c-q
    coins = coins +1
while c >= p:
    c = c - p
    coins = coins + 1
while  c >= n:
    c = c - n
    coins = coins + 1
while  c >= c1:
    c = c - c1
    coins = coins + 1

print(coins)
        

        