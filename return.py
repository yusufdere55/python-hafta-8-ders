def toplama(a,b):
    return a+b

x = int(input("1. Sayıyı girin: "))
y = int(input("2. Sayıyı girin: "))

sonuc = toplama(x,y)

print(sonuc)

def cikarma():
    s1 = int(input("1. Sayıyı girin: "))
    s2 = int(input("2. Sayıyı girin: "))
    return s1-s2

sonuc1 = cikarma()
print(sonuc1)

#Hem parametersiz hem de parametreli olarak geri döndüren bir fonksiyon tanımlanabilir.
#Yukarıdaki toplama parametreli iken çıkarma işlemi parametresiz olarak tanımlanmıştır.
