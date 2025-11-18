#kullanıcadan sayı girdisi al 1,2,3,4,5,6,7
#bu sayılar toplama, çıkarma, çarpma, bölme, karesini alma, kök bulma, ve son olarak 7.de ise yanlış girdiniz diye tekrar soracak.
#hepsi için ayrı fonksiyonlar oluşturacaksın
#iki parametresi olacak, işlemleri basit bir şekilde yapacak
#decimal
#karesini alma ve kök bulma içinde tek parametreli birer fonksiyon oluşturacaksın ve bunlar tek işlem yapacak
#aynı sayıyı kendine bölüp kökünü bulcak, ya da karesiyle çarpıp karesini alacak
#ve bunun çıktısını verecek

# Çift parametreli işlemler
def toplama(num1,num2):
    return num1+num2

def cikarma(num1,num2):
    return num1-num2
    
def carpma(num1,num2):
    return num1*num2

def bolme(num1,num2):
    if num2 == 0:
        return "HATA: Sıfıra bölünemez."
    return num1/num2
    
# Tek parametreli işlemler    
def karesi(num1):
    return num1 ** 2

def karekok(num1):
    if num1 < 0:
        return "HATA: Negatif sayıların karekökü alınmaz."
    return num1 ** 0.5


print("                              ********** HESAP MAKİNESİ **********")
print(" ")
print("            İşlemler: 1-Toplama 2-Çıkarma 3-Çarpma 4-Bölme 5-Karesi 6-Karekök  ")
print(" ")


# *** TÜM PROGRAM DÖNGÜ İÇİNDE ***
while True:

    # İşlem seçimi
    while True:
        try:
            islem = int(input("Yapmak istediğiniz işlemin numarasını girin: "))
            break
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")

    # İşlemi uygula
    match islem:
        case 1:
            print("Toplama")
            num1=float(input("Birinci sayıyı giriniz: "))
            num2=float(input("İkinci sayıyı giriniz: "))
            sonuc = toplama(num1,num2)

        case 2:
            print("Çıkarma")
            num1=float(input("Birinci sayıyı giriniz: "))
            num2=float(input("İkinci sayıyı giriniz: "))
            sonuc = cikarma(num1,num2)

        case 3:
            print("Çarpma")
            num1=float(input("Birinci sayıyı giriniz: "))
            num2=float(input("İkinci sayıyı giriniz: "))
            sonuc = carpma(num1,num2)

        case 4:
            print("Bölme")
            num1=float(input("Birinci sayıyı giriniz: "))
            num2=float(input("İkinci sayıyı giriniz: "))
            sonuc = bolme(num1,num2)

        case 5:
            print("Karesini Alma")
            num1=float(input("Sayıyı giriniz: "))
            sonuc = karesi(num1)

        case 6:
            print("Kök bulma")
            num1=float(input("Sayıyı giriniz: "))
            sonuc = karekok(num1)

        case _:
            print("Geçersiz seçim.")
            continue

    # Sonucu yazdır
    print("Sonuç:", sonuc)

    # Devam etmek
    while True:
        devam = input("İşlem yapmaya devam etmek istiyor musunuz? E/H: ").upper()
        if devam == "E":
            break   # dıştaki while True döngüsüne döner
        elif devam == "H":
            print("Çıkış")
            exit()
        else:
            print("HATA: Lütfen geçerli harfleri giriniz.")
