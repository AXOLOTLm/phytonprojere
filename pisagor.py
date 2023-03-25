x = int(input("Bir Sayı Giriniz:"))
n = 1


def pisagor(x):
    for a in range(1, x + 1):
        for b in range(1, x + 1):
            for c in range(1, x + 1):
                if (c ** 2 == a ** 2 + b ** 2):
                    if n == a + b + c:
                        continue

                    else:
                        print(a, b, c)
                        n = a + b + c

                else:
                    continue


pisagor(x)
