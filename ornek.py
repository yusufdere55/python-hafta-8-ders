#soru1:

def ciftoralama(l,k):
    toplam=0
    ortalama=0
    sayac=0
    for i in range(l,k+1,1):
        if(i%2==0):
            toplam=toplam+i
            sayac=sayac+i
    ortalama=toplam/sayac
    return ortalama

s1=int(input("Başlangıç sayısını giriniz: "))
s2=int(input("Bitiş sayısını giriniz: "))
son = ciftoralama(s1,s2)
print(son)


#soru2:

def ortalama(a,b,x,y):
    ort = (vize * (vizeort/100)) + (final * (finalort/100))
    return ort

vize = int(input("Vize notunu giriniz: "))
vizeort = float(input("Vize oranını giriniz:"))

final = int(input("Final notunu giriniz: "))
finalort = int(input("Final oranını giriniz:"))

sonuc = ortalama(vize,vizeort,final,finalort)
print(sonuc)