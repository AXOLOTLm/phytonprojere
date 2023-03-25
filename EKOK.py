


def EKOK(sayı1,sayı2):
    ortak = []
    carpim = sayı2*sayı1
    for i in range(2,sayı1+1):
       for j in range(2,sayı2+1):
        if sayı1 % i == 0 and sayı2 % i == 0 and i == j :
            carpim *= i

            carpim.append(i)

    print()


