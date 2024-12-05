import random

n = int(input("n sonini kiriting: "))

tanlanganSon = random.randint(1, n)

urinishlar = 3

for i in range(1, urinishlar + 1):
    tahmin = int(input(f"{i}-urinish:  "))
    
    if tahmin == tanlanganSon:
        print("Winner!")
        break
    else:
        print("Noto'g'ri")

if tahmin != tanlanganSon:
    print("Looser!")
