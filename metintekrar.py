# Benim Yaptığım
def metintekrar():
    sayac = 0
    while(sayac < tekrar):
        sayac = sayac+ 1
        print(sayac , " " + metin)

metin = input("Metin girin:")
tekrar = int(input("Tekrar Sayısı:"))

metintekrar()

#Hocanın yaptığı
metin2 = input("Metin girin:")
tekrar2 = int(input("Tekrar Sayısı:"))

def yazdir(x,y):
    for i in range(1,y+1):
        print(x,end="\n")

yazdir(metin2,tekrar2)