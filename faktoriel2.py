#recursive fonksiyon: fonksiyon içinde kendisini çağırarak çalıştırılabilir fonksiyondur.

def faktroiel(sayi):
    if sayi == 1:
        return sayi
    else:
        return sayi*faktroiel(sayi-1)

deger = int(input("Sayı giriniz: "))
son = faktroiel(deger)
print(son)