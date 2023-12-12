def asalmi(sayi):
    sayac = 2 
    toplama = 0 
    while sayac<=int(sayi/2):
        if(sayi % sayac == 0):
            toplama+=1
        sayac+=1

    if(toplama==0):
        print("Sayı Asal")
    else:
        print("Sayı Asal Değil")

sayi = int(input("Kontrol edilecek sayıyı giriniz: "))

asalmi(sayi)