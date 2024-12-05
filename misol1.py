son = int(input("Son kiriting: "))

for i in range(2, son):
    tub = True
    for j in range(2, i):
        if i % j == 0:
            tub = False
            break
    if tub:
        print(i, end=" ")

