for i in range(100, 1000):
    yuzlik_son = i // 100
    onlik_son = (i // 10) % 10
    birlik_son = i % 10
    
    if yuzlik_son == onlik_son or yuzlik_son == birlik_son or onlik_son == birlik_son:
        print(i, end=", ")
