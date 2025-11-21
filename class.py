# Methodlar (def sum gibi) yani yöntemler, class içinde tanımlandığında function (fonksiyon) ismini alır.
# Bir sınıf (class), kendisinden örnek oluşturulabilen bir nesnedir (object). Bu sınıflara özellik ve yöntemler atanabilir.
# init method’u ( __init__() Function). Tanımlayacağınız bütün sınıfların __init__() method’u vardır. 
# Nesne ilk oluşurken __init__() method’u her zaman yürütülür. Bu ilk method çağrıldığında, sizin belirli özellikler ile başlasın dediğiniz özellikler atanır.
# __init__(...): Bu, sınıfın yapıcı (constructor) metodudur. Bir Kisi nesnesi oluşturulduğunda otomatik olarak çalışan fonksiyondur.
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


































