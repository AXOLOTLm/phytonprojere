print("""*************************************************************

                              SEÇENEKLER

1 BAKİYE 

2 PARA YATIRMA

3 PARA ÇEKME

ÇIKIŞ İÇİN "q" ya BASIN

***********************************************************************""")

bakiye = 1000

while True:
    işlem = input("işlem Seçiniz:")

    if (işlem == "q"):
        print("YİNE BEKLERİZ :) ")
        break

    elif (işlem == "1"):
        print("Bakiyeniz {} TL dir".format(bakiye))

    elif (işlem == "2"):
        miktar = int(input("Miktarı Giriniz:"))

        if (miktar < 0):
            print("Bunu Yapamazsınız...")

        bakiye += miktar

    elif (işlem == "3"):
        miktar = int(input("Miktarı Giriniz:"))

        if (miktar < 0):
            print("Bunu Yapamazsınız...")


        if (bakiye - miktar < 0):
            print("Yetersiz Bakiye......")

        bakiye -= miktar

    else:
        print("İşlem Geçersiz..............")



