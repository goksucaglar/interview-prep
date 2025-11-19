#recursive fonksiyonların çalışma mantığı
#big o nedir, nasıl hesaplanır
#recursive in big o ya etkisi nedir araştır
#recursive ve recursive olmayan fibonaccinin kullanıcıdan alınan n. elamanını bulan kod
#matematiksel formulü kendin uygula, yapay zeka yok
#bitiş 20 kasım perşembe saat 10


#Recursive fonksiyonlar(özyinelemeli fonksiyonlar): kendi kendini tekrar kullanan fonksiyonlardır.
#bu fonksiyonun bir yerde durması gerekir buna base case(temel durum) denir.
# def recurse():
#    ...
#    recurse()
#    ...
# recurse()
#

#a = factorial(3)
#
#def factorial(n):
#  if n == 1:
#    return 1
#  else:
#    return 1 * factorial(n-1)


#Big-O notasyonu bir algoritmayı analiz etmede kullanılan en temel araçlardan bir tanesidir.
#Argümanın belirli bir değere veya sonsuzluğa yaklaşması durumunda bir fonksiyonun sınırlayıcı davranışını tanımlayan matematiksel bir gösterim.
#O harfinin kullanılması fonksiyonun order'ı ile ilgilidir.
#Basitçe, Big-O notasyonu; cebirsel ifadeler kullanarak kodunuzun karmaşıklığını açıklar.
#Algoritmaların çalışma süresi Big-O notasyonu ile ifade edilir.
#Time complexity: Bir algoritmanın çalışması için geçerli olan süredir. Bu süre kaç tane işlem gerçekleştiğine bağlı olarak hesaplanır. Veri seti büyüklüğüne
#Bize 3 durum sunar. Best, average, worst-case.
#Big-O için; c=sabit değer, n=veri seti büyüklüğü ya da eleman sayısı 
# O(1)-> CONSTANT (good)
# O(N)-> LINEAR (fair)
# O(N^2)-> QUADRATIC (horrible)
# O(log N)-> LOGARITHMIC (good)
# O(N log N)-> LINEARITHMIC (bad)
# O(c^N)-> EXPONENTIAL (horrible)
# O(N!)-> FACTORIAL (horrible)
#
# O(1)-> CONSTANT Complexity: Veri seti ne kadar büyük olursa olsun, çalıştırılma süresi ve kullanılan kaynak sayısı sabittir. Örnek: Tek mi çift mi bulma, dizinin son elemanını bulma.
# O(N)-> LINEAR Complexity: Veri seti arttıkça, çalışma süreside doğru orantılı şekilde artar. Örnek: Bir dizinin tüm elemanlarını yazdırma.
# O(N^2)-> QUADRATIC Complexity: Girdi büyüklüğünün karesi ile doğru orantılıdır. Eğer input değeri 2 ise 4 işlem gerçekleşir. 
#        Örnek: Sorting(sıralama) algoritmalarında. Bir array içerisindeki her elemanı, arrayin diğer elemanları ile yazdırma. İç içe döngü.
# O(log N)-> LOGARITHMIC Complexity: Her seferinde problemi ikiye bölen algoritmalarda. Örnek: Binary Search 
# O(c^N)-> EXPONENTIAL Complexity: Girdi N büyüklüğünde ise output 2^N olur. Örnek: Verilen bir stringin tüm alt kümelerini hesaplama.
# O(N!)-> FACTORIAL Complexity: Tipik olarak tüm permütasyonları denemek zorunda olan algoritmalarda görülür. 
#        Örnek: Şifre kırma algoritmaları, gezgin satıcı problemleri(TSP) (Brute-force, Bir porblemi çözmek için, bütün olasılıkları dener.)
# O(N log N)-> LINEARITHMIC Complexity: Bir algoritmanın çalışma süresinin N ve log N'in çarpımı oranında arttığını söyler. 
#        N: elemanların sayısı(iş miktarı artıyor), log N: her adımda parçalama/kıyaslama sürecini gösteriyor. İki şey birlikte büyüyor-> linearithmic 
#        Örnek: Bir listeyi sıralamak (Timsort, Quick sort, Heap Sort, Merge Sort)     -Hem lineer büyüyen iş miktarı hem de logaritmik büyüyen bölünmeler içeren zaman karmaşıklığı.-

#recursive ve recursive olmayan fibonaccinin kullanıcıdan alınan n. elamanını bulan kod
# Fibonacci: Her bir terimin kendinden bir önceki ve iki önceki teriminin toplamı. İlk iki terimin 1 olduğunu belirleriz. 
#            Base case n<=2 olması ve 1 döner. n>2 olduğunda recursive fonk. her bir çağırmada base case'e inene kadar çalışır.


# fibonacci dizi: 1,1,2,3,5,8,11
n = int(input("kaçıncı fibonacci sayısını istiyorsunuz?: ")

def fibonacci(n):
  if n<=2:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)
          





































