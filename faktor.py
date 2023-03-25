print("""****************************

    Faktoriyel Bulma İşlemi


Çıkmak İçin "q" ya basın
********************************""")

while True:
    sayı = input("Sayı:")
    if (sayı == "q"):
        print("Program Sonlandırıldı...")
         break

    else:
        sayı = int(sayı)

        faktoriyel = 1

        for i in range (2,sayı+1):
            print("Faktoriyel",faktoriyel,"i:".i)
            faktoriyel += 1
        print("Faktoriyel",faktoriyel)