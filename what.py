print("""*******************************************
               MİNECRAFT
               HESAP GİRİŞİ
***********************************""")





sys_kullanıcı ="AXO"
sys_parola ="21082017"
giris_hakkı = 3
while True:
    kullanıcı_ad =input("Kullanıcı Ad:")
    parola = int(input("Parola:"))

    if (sys_kullanıcı != kullanıcı_ad and sys_parola == parola):
        print("Hatalı Kullanıcı Adı")
        giris_hakkı -= 1

    elif (sys_kullanıcı ==kullanıcı_ad and sys_parola != parola):
        print("Hatalı Parola")
        giris_hakkı -= 1

    elif (sys_kullanıcı != kullanıcı_ad and sys_parola != parola):
        print("İkiside Hatalı")

    else:
        print("Doğrulandı")
        break

    if (giris_hakkı == 0):
        print("Giriş Hakkı Bitti")
        break
