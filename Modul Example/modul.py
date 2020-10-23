# Matematiksel Hesaplama Münüsü
def topla(sayi1,sayi2):
    """
    Topla iki sayinin toplamini veren foksiyondur.
    """
    return sayi1 + sayi2
def çıkar(sayi1,sayi2):
    """
    Çıkar iki sayinin farkini veren foksiyondur.
    """
    return sayi1 - sayi2
def böl(sayi1,sayi2):
    """
    Böl iki sayinin bolumunu veren foksiyondur.
    """
    return sayi1/sayi2
def çarp(sayi1,sayi2):
    """
    Çarp iki sayinin çarpimini veren foksiyondur.
    """
    return sayi1 * sayi2
def mod(sayi1,sayi2):
    """
    Mod iki sayidan birinin digerine bolumunden kalani veren fonksiyondur.
    """
    return sayi1 % sayi2
def üs(sayi1,sayi2):
    """
    Üs bir sayinin diger sayi kadar ussunu veren fonksiyondur.
    """
    return pow(sayi1,sayi2)

# Geometrik Hesaplama Menüsü
def kare(kenar):
    """
    Bir karenin alan çervresimi veren fonksiyon.
    """
    return f"""
    Karenin Kenarı  : {kenar}
    Karenin Alanı   : {kenar*kenar}
    Karenin Çevresı : {4*kenar}
    """
def dikdortgen(kisakenar,uzunkenar):
    """
    Bir dikdortgenin alan ve çevresini veren fonksiyon.
    """
    return f"""
    Dikdörtgenin Uzun Kenarı : {uzunkenar}
    Dikdörtgenin Kisa Kenarı : {kisakenar}
    Dikdörtgenin Alanı       : {kisakenar*uzunkenar}
    Dikdörtgenin Çevresi     : {2*uzunkenar + 2*kisakenar}
    """
def  dikuçgen(dikkenar,taban,hipotenus):
    """
    Bir dik uçgenin alanini ve çevresini veren fonksiyon.
    """
    return f"""
    Uçgenin Dik Kenar Uzunlugu : {dikkenar}
    Uçgenin Taban Uzunlugu     : {taban}
    Uçgenin Hipotenus uzunluğu : {hipotenus}
    Uçgenin Alani              : {taban * (dikkenar/2)}
    Uçgenin Çevresi            : {taban  + dikkenar + hipotenus}
    """
def ikizkenaruçgen(esitkenar,yukseklik,taban):
    """
    Bir ikizkenar uçgenin alani ve çevresini veren fonksiyon.
    """
    return f"""
    Uçgenin Esit Kenar Uzunlugu : {esitkenar}
    Uçgenin Yuksekligi          : {yukseklik}
    Uçgenin Taban Uzunlugu      : {taban}
    Uçgenin Alani               : {yukseklik * (taban / 2)}
    Uçgenin Çevresi             : {taban + (2 * esitkenar)}
    """
def daire(yariçap):
    """
    Bir dairenin alani ve çevresini veren fonksiyon.
    """
    return f"""
    Dairenin Yariçap Uzunlugu : {yariçap}
    Dairenin Alani            : {2 * 3.14 * yariçap}
    Dairenin Çevresi          : {3.14 * pow(yariçap,2)}
    """
def elips(kisacap,uzuncap):
    """
    Bir elipsin cevresi ve alanini veren fonksiyon.
    """
    return f"""
    Elipsin Kisacap Uzunlugu : {kisacap}
    Elipsin Uzuncap Uzunlugu : {uzuncap}
    Elipsin Alani            : {3.14 * uzuncap * kisacap}
    Elipsin Çevresi          : {2 * 3.14 *pow((pow(uzuncap,2)+pow(kisacap,2))/2 , 1/2) }
    """
def paralelkenar(uzunkenar,kisakenar,yukseklik):
    """
    Bir paralelkenarin cevresi ve alanini veren fonksiyon.
    """
    return f"""
    Paralelkenarin Kisakenar Uzunlugu : {kisakenar}
    Paralelkenarin Uzunkenar Uzunlugu : {uzunkenar}
    Paralelkenarin Yuksekligi         : {yukseklik}
    Paralelkenarin Alani              : {uzunkenar * yukseklik}
    Paralelkenarin Cevresi            : {2 * uzunkenar + 2 * kisakenar}
    """