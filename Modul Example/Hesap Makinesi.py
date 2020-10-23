from modul import *
import time

print("""
-------------------------------------------
|  Geomerik ve Aritmetik Hesap Makinesi   |
-------------------------------------------
| A)Geometrik Menü (Alan ve Çevre Hesabı) |
-------------------------------------------
| 1-Kare            | 2-Diküçgen          |
| 3-Dikdörtgen      | 4-İkizkenar Üçgen   |
| 5-Daire           | 6-Elips             |
| 7-Paralelkenar    |                     |
-------------------------------------------
|          B)Aritmetik Menü               |
-------------------------------------------
| 1-Toplama         | 2-Çıkarma           |
| 3-Çarpma          | 4-Bölme             |
| 5-Üs Alma         | 6-Mod Alma          |
-------------------------------------------
Programı kapamak isterseniz (q) ya basın.
""")
while True:
    işlem=input("Lütfen yapacağınız işlemin menüsünü seçiniz: ")
    if işlem =="q":
        print("Program kapatılıyor....")
        time.sleep(1)
        print("Programdan çıkışınız gerçekleşmiştir.")
        break
    else:
        if işlem =="A" or işlem =="a":
            işlem2=int(input("Lütfen yapacağınız işlemi seçiniz: "))
            if işlem2 == 1:
                kenar=int(input("Lütfen karenin bir kenarını giriniz: "))
                time.sleep(1)
                print(kare(kenar))
            elif işlem2 == 2:
                taban=int(input("Lütfen üçgenin taban uzunluğunu giriniz: "))
                dikkenar=int(input("Lütfen üçgenin dikkenar uzunluğunu giriniz: "))
                hipotenüs=int(input("Lütfen üçgenin hipotenüs uzunluğunu giriniz: "))
                time.sleep(1)
                print(dikuçgen(dikkenar,taban,hipotenüs))
            elif işlem2== 3:
                uzunkenar = int(input("Lütfen dikdörtgenin uzunkenarının uzunluğunu giriniz:"))
                kısakenar = int(input("Lütfen dikdörtgenin kısakenarının uzunluğunu giriniz:"))
                time.sleep(1)
                print(dikdortgen(kısakenar,uzunkenar))
            elif işlem2 == 4:
                kenar = int(input("İkizkenar üçgenin kenar uzunluğunu giriniz: "))
                yukseklik =int(input("İkizkenar üçgenin yüksekliğini giriniz: "))
                taban = int(input("İkizkenar üçgenin taban uzunluğunu giriniz: "))
                time.sleep(1)
                print(ikizkenaruçgen(kenar,yukseklik,taban))
            elif işlem2 == 5:
                çap = int(input("Dairenin yarıçapının uzunluğunu giriniz: "))
                time.sleep(1)
                print(daire(çap))
            elif işlem2 == 6:
                kısayarıçap = int(input("Elipsin kısa yarıçapının uzunluğunu giriniz: "))
                uzunyarıçap = int(input("Elipsin uzun yarıçapının uzunluğunu giriniz: "))
                time.sleep(1)
                print(elips(kısayarıçap,uzunyarıçap))
            elif işlem2 == 7:
                uzunkenar = int(input("Paralelkenarın uzun kenarını giriniz: "))
                kısakenar = int(input("Paralelkenarın kısa kenarını giriniz: "))
                yükseklik = int(input("Paralelkenarın yüksekliğini giriniz:"))
                time.sleep(1)
                print(paralelkenar(uzunkenar,kısakenar,yükseklik))
            else:
                time.sleep(1)
                print("Hatalı giriş yaptınız.Lütfen tekrar deneyiniz.")
        elif işlem == "B" or işlem == "b":
            işlem3=int(input("Lütfen yapacağınız işlemi seçiniz: "))
            if işlem3 == 1:
                sayı1 = int(input("1.sayıyı giriniz: "))
                sayı2 = int(input("2.sayıyı giriniz: "))
                time.sleep(1)
                print(topla(sayı1,sayı2))
            elif işlem3 == 2:
                sayı1 = int(input("1.sayıyı giriniz: "))
                sayı2 = int(input("2.sayıyı giriniz: "))
                time.sleep(1)
                print(çıkar(sayı1,sayı2))
            elif işlem3 == 3:
                sayı1 = int(input("1.sayıyı giriniz: "))
                sayı2 = int(input("2.sayıyı giriniz: "))
                time.sleep(1)
                print(çarp(sayı1,sayı2))
            elif işlem3 == 4:
                sayı1 = int(input("1.sayıyı giriniz: "))
                sayı2 = int(input("2.sayıyı giriniz: "))
                time.sleep(1)
                print(böl(sayı1,sayı2))
            elif işlem3 == 5:
                sayı1 = int(input("Taban sayıyı giriniz: "))
                sayı2 = int(input("Üssünü giriniz: "))
                time.sleep(1)
                print(üs(sayı1,sayı2))
            elif işlem3 == 6:
                sayı1 = int(input("Mod alınacak sayıyı giriniz: "))
                sayı2 = int(input("Modun değerini giriniz: "))
                time.sleep(1)
                print(mod(sayı1,sayı2))
            else:
                time.sleep(1)
                print("Hatalı giriş yaptınız.Lütfen tekrar deneyiniz.")





               

