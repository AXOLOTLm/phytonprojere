
def EBOB(sayi1,sayi2):
    carpim = []
    for i in range(2,sayi1+1):
       for j in range(2,sayi2+1):
        if sayi1 % i == 0 and sayi2 % i == 0 and i == j:
            carpim *= i

            carpim.append(i)

    print(carpim[-1])


EBOB(100,205)