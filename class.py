# Methodlar (def sum gibi) yani yöntemler, class içinde tanımlandığında function (fonksiyon) ismini alır.
# Bir sınıf (class), kendisinden örnek oluşturulabilen bir nesnedir (object). Bu sınıflara özellik ve yöntemler atanabilir.
# init method’u ( __init__() Function). Tanımlayacağınız bütün sınıfların __init__() method’u vardır. 
# Nesne ilk oluşurken __init__() method’u her zaman yürütülür. Bu ilk method çağrıldığında, sizin belirli özellikler ile başlasın dediğiniz özellikler atanır.
# __init__(...): Bu, sınıfın yapıcı (constructor) metodudur. Bir Kisi nesnesi oluşturulduğunda otomatik olarak çalışan fonksiyondur.
# Yapıcı (constructor) metodud, bir sınıftan yeni bir nesne oluşturulduğunda otomatik olarak çalışan özel bir fonksiyondur.
# Yani bir sınıf içerisinde ilk çalışan method olur kendileri.
# self.name -> self: Python dilinde geçerli bir terimdir, tanımladığınız sınıfta yer alan herhangi bir değişkene veya diğer method’lara erişmek için selfkullanırız. 
# Method’lara ve değişkenlere self olmadan erişemezsiniz. 
# @staticmethod keyword’ü ile tanımladığınız methodlara, self olmadan erişmek mümkün.
# self bir sınıf içerisinde iken kullanılır, methodlara ve değişkenlere erişim bununla sağlanır.

class Car:
  def __init__(self, name, type, engine, hp):
    # Bu satır, parametre olarak gelen isim ve yas değerlerini nesneye ait özelliklere aktarır.
    self.name = name
    self.type = type
    self.engine = engine
    self.hp = hp
    self.tire_count = 4

car1 = Car("Ferrari", "Sport Car", "Gasoline", 4000)
car2 = Car("Tofaş", "Basic Car", "LPG", 1600)
  
print(car1.name, car1.type, car1.engine, car1.hp, car1.tire_count)
print(car2.name, car2.type, car2.engine, car2.hp, car2.tire_count)

# örnek

class Kisi:
  def __init__(self, isim, yas):
    self.isim = isim
    self.yas = yas
  def yazdir(self):
    print("Merhaba, adım ", self.isim, ", yaşım ", self.yas);

p1 = Kisi("Murat", 36)
p1.yazdir()


# Static method → Nesneye değil, doğrudan sınıfa aittir.
# Yani böyle çağırılabilir. araba.calistir()
# Nesne oluşturman gerekmez.
# Örneğin; Her araba için aynı işlemi yapıyorsa, sadece genel bir işlem yapıyorsa @staticmethod kullanılır.
# Bir arabanın, kendi rengini, kendi modelini, kendi hızını, kullanıyorsan, o zaman nesnenin özelliklerine ihtiyacın vardır. self kullanırsın.

# @staticmethod
class araba:
    @staticmethod
    def calistir():
        araba.durdur()

    @staticmethod
    def durdur():
        print "durdu"



# Nesneler oluştuktan sonra belli duruma (state’e) sahip olurlar.
# Nesneler yine oluşturulduktan itibaren memoryde yer almaya başlarlar.
# Bir sınıfın birden fazla nesnesi olabilir ve hepsi farklı özellikler gösterirler.
# Nesneler, sınıflardan oluşturulur ve sınıflar var olmadan var olamazlar. Yani bir sınıftan oluşmayan bir nesne olamaz.

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Üst Sınıf
class Top:
    def __init__(self, renk = "Beyaz", marka = "Nike"):
      self.renk = renk
      self.marka = marka
    def patla(self):
      print(f"{self.marka} marka ve {self.renk} renkli top patladı!")

# Alt Sınıflar
# 1
class BasketTopu(Top):
    def __init__(self, renk = "Turuncu", marka = " Visa ", hava_basinci = 100, basket_sayisi = 0):
      super().__init__(renk, marka) # Üst sınıfın özelliklerini ekliyor
      # super() → “Alt sınıfım, üst sınıfın metodunu/özelliğini kullanmak istiyorum” demenin yolu.
      self.hava_basinci = hava_basinci
      self.basket_sayisi = basket_sayisi
    def basket_ol(self):
      self.basket_sayisi += 1
      print("Basket Sayısı: ", self.basket_sayisi)
    def patla(self):
      self.basket_sayisi = 0
      print("Basket Sayısı: ", self.basket_sayisi)
# 2
class VoleybolTopu(Top):
    def __init__(self, renk = "Sarı-Mavi", marka = "İş Bankası" , agirlik = 50, sayi = 0):
      super().__init__(renk, marka)
      self.agirlik = agirlik
      self.sayi = sayi
    def sayi_kazan(self):
      self.sayi += 1
      print("Kazanılan Sayı: ", self.sayi)
    def patla(self):
      self.sayi = 0
      print("Kazanılan Sayı: ", self.sayi)

# 3
class FutbolTopu(Top):
    def __init__(self, renk = "Beyaz-Siyah", marka = "Fenerbahçe" , agirlik = 50, gol_sayisi = 0):
      super().__init__(renk, marka)
      self.agirlik = agirlik
      self.gol_sayisi = gol_sayisi
    def gol_ol(self):
      self.gol_sayisi += 1
      print("Gol Sayısı: ", self.gol_sayisi)
    def patla(self):
      self.gol_sayisi = 0
      print("Gol Sayısı: ", self.gol_sayisi)

# 4
class HentbolTopu(Top):
    def __init__(self, renk = "Beyaz" , marka = "MasterCard", agirlik = 30 , skor = 0):
      super().__init__(renk, marka)
      self.agirlik = agirlik
      self.skor = skor
    def skor_al(self):
      self.skor += 1
      print("Skor sayısı: ", self.skor)

# Ana Program
def main():
    print("Seçenekler: 1-Basketbol Topu, 2-Voleybol Topu, 3-Futbol Topu, 4-HentbolTopu")
    print(" ")
    secim = input("Seçiminiz (1/2/3/4): ")
    
    if secim == "1":
      renk = input("Topun rengi: ")
      # renk = input("Topun rengi: ") or "Turuncu"
      # Kullanıcı "Kırmızı" yazarsa → renk = "Kırmızı"
      # Kullanıcı sadece Enter basarsa → renk = "Turuncu"
      marka = input("Topun markası: ") 
      hava_basinci = int(input("Hava Basıncı: "))
      basket_sayisi = int(input("Basket Sayısı: "))
      top = BasketTopu(renk, marka, hava_basinci, basket_sayisi)
      top.basket_ol()
      
    elif secim == "2":
      renk = input("Topun rengi: ")
      # renk = input("Topun rengi: ") or "Sarı-Mavi" böyle de yazılabilir
      marka = input("Topun markası: ") 
      agirlik = float(input("Ağırlık: "))
      sayi = int(input("Sayı: "))
      top = VoleybolTopu(renk, marka, agirlik, sayi)
      top.sayi_kazan()
    
    elif secim == "3":
      renk = input("Topun rengi: ") 
      marka = input("Topun markası: ") 
      agirlik = float(input("Ağırlık: ")) 
      gol_sayisi = int(input("Gol Sayısı: ")) 
      top = FutbolTopu(renk, marka, agirlik, gol_sayisi)
      top.gol_ol()

    elif secim == "4":
      renk = input("Topun rengi: ")
      marka = input("Topun markası:")
      agirlik = float(input("Ağırlık: "))
      skor = int(input("Skor: "))
      top = HentbolTopu(renk, marka, agirlik, skor)
      top.skor_al()
    
    else:
      print("Geçersiz seçim.")
      return

    # Ortak metodu çağır
    top.patla()
  
# Programı başlat
main()
      
    
 


# Top adında bir üst (temel) sınıf tanımlayınız. Bu sınıfta tüm toplar için ortak olabilecek en az bir özellik olsun (örneğin renk, marka vb.) ve patla() adında bir metot bulunsun. 
# Top sınıfından kalıtım alan üç alt sınıf tanımlayınız: BasketTopu, VoleybolTopu ve FutbolTopu. Bu sınıflar için:    
    
# a. BasketTopu sınıfı için:
# i. hava_basinci ve basket_sayisi adında örnek değişkenleri oluşturunuz.    
# __init__ (constructor) metodunda hava_basinci için sabit bir başlangıç değeri atayınız ve basket_sayisi değişkenine 0 atayınız.    
# ii. basket_ol() isimli bir metot yazınız. Bu metot basket_sayisi değerini artırmalı ve yeni değeri ekrana yazdırmalıdır.
    
# b. FutbolTopu sınıfı için:
# i. agirlik ve gol_sayisi örnek değişkenlerini oluşturunuz.
# __init__ metodunda agirlik için sabit bir başlangıç değeri atayınız ve gol_sayisi değişkenine 0 atayınız.  
# ii. gol_ol() isimli bir metot yazınız. Bu metot gol_sayisi değerini artırmalı ve yeni değeri ekrana yazdırmalıdır.
    
# c. VoleybolTopu sınıfı için: 
# i. agirlik ve sayi örnek değişkenlerini oluşturunuz.
# __init__ metodunda agirlik için sabit bir başlangıç değeri atayınız ve sayi değişkenine 0 atayınız.
# ii. sayi_kazan() isimli bir metot yazınız. Bu metot sayi değerini artırmalı ve yeni değeri ekrana yazdırmalıdır.
    
# d. Bu sınıfların __init__ metotlarını (constructor) mutlaka tanımlayınız.
# Kullanıcıdan alınmayan (giriş yapılmayan) alanlara __init__ içinde uygun varsayılan (default) değerler atayınız.

# Oluşturulan sınıflarda (BasketTopu, VoleybolTopu ve FutbolTopu) Top sınıfından miras alınan patla() metodunu override ediniz.
# Override edilen patla() metodu çalıştığında, ilgili topun tuttuğu sayı değişkeninin (basket_sayisi, gol_sayisi veya sayi) değerini 0 yapmalıdır.


# main.py dosyasında bir ana program yazınız. Program kullanıcıyla etkileşimli olmalıdır. Örneğin:


# Kullanıcıya hangi tip top oluşturmak istediği sorulsun (basketbol, voleybol, futbol).


# Seçilen top türüne göre, o topa ait özellikler kullanıcıdan input() ile tek tek alınsın.


# Alınan bilgilere göre ilgili sınıftan bir nesne oluşturulsun.

# Top sınıfından türeyen yeni bir sınıf daha tanımlayınız (örneğin HentbolTopu).
# Bu sınıfa kendine özgü en az bir özellik ve metot ekleyerek sınıfı geliştiriniz.
































