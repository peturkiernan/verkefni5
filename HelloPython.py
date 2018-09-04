top_num = int(input("Input a number between 0 and 999: "))

for i in range(0,top_num):
    if (i > 0) & (i < 10):
        tala1 = i ** 1
        if tala1 == i:
            print(i)
    elif (i >= 10) & (i < 100):
        tala1 = (i // 10) ** 2
        tala2 = (i % 10) ** 2
        if (tala1 + tala2) == i:
            print(i)
    elif (i >= 100) & (i < 1000):
        tala1 = (i // 100) ** 3
        tala2 = ((i // 10) % 10) ** 3
        tala3 = (i % 10) ** 3
        if (tala1 + tala2 + tala3) == i:
            print(i)
    
        