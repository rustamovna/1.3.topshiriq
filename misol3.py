n = int(input("Son kiriting: "))

summa = 0

for i in range(1, n + 1):
    summa += i * i  

    if i < n:
        print(f"{i}^{i} + ", end="")
    else:
        print(f"{i}^{i} = {summa}")




