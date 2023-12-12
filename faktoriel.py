def faktoriyel(sayi):
    sonuc=1
    if(sayi==0 or sayi==1):
        return sonuc
    elif(sayi>=1):
        for i in range(1,sayi+1,1):
            sonuc*=i
        return sonuc
    else:
        print("0 veya daha büyük sayı girmelisiniz")

deger=int(input("Sayı giriniz: "))
son = faktoriyel(deger)
print(son)