#bir fonksiyon başka bir fonskiyon içinde çağıralarak kullanılabilir.

def yashesap(dogumyili):
    return 2023 - dogumyili
def emeklilik(dogumyili):
    yas = yashesap(dogumyili)
    emeklilik=65-yas
    print("Emekliliğinize" , emeklilik, "Yıl Kalmıştır")

emeklilik(2003)