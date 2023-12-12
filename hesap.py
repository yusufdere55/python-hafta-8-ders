s1 = int(input("1. Sayıyı giriniz:"))
s2 = int(input("2. Sayıyı giriniz:"))

tur = int(input("İşlem seçiniz(t=1,çıkarma=2,b=3,ç=4)"))

def toplama(s1,s2):
    sonuc = s1 + s2
    print(sonuc)

def cikarma(s1,s2):
    sonuc = s1 - s2
    print(sonuc)

def bolme(s1,s2):
    sonuc = s1 / s2
    print(sonuc)

def carpma(s1,s2):
    sonuc = s1 * s2
    print(sonuc)


if(tur == 1):
    toplama(s1,s2)

elif(tur == 2):
    cikarma(s1,s2)
    
elif(tur == 3):
    bolme(s1,s2)


elif(tur == 4):
    carpma(s1,s2)