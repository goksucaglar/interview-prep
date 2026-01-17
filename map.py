# "Robot Koloni Simülasyonu - Pathfinding + Strategy Al"
# Ödev Özeti
# Bir 2D harita üzerinde yaşayan robotlardan oluşan bir koloni simüle edeceksin.
# Robotlar:
# Haritada dolaşacak
# Engellerden kaçacak
# Kaynaklar toplayacak
# Bir strateji algoritmasıyla karar verecek
# Pathfinding (A*, BFS veya Dijkstra zorunlu) kullanacak
# Tüm sistem OOP ile tasarlanacak.

# 1. Başlangıçta ne oluyor?
# 2. Süreç boyunca tekrar eden işlem ne?
# 3. Ne zaman bitiyor?

# ÇEVRE ALGILAMA
# - Yakında engel var mı?
# - Kaynak var mı?
# - Robot var mı?
# - Üs ne tarafta?

# HEDEF SEÇME
# - Kaynak mı toplayacak?
# - Üsse mi dönecek?
# - Engel mi var, kaçınmalı mı?
# - Keşif mi yapacak?

# YOL HESAPLAMA
# - engellere çarpmamak
# - en kısa yolu bulmak
# - tıkanınca yeniden hesaplamak

# HAREKET

# ENERJİ AZALTMA
# - yürüdükçe enerji harcar
# - taşıdıkça daha da harcar

# OLAY KONTROLÜ
# - Kaynağın üzerine geldiyse → toplamalı
# - Engel varsa → çarpışma kontrolü
# - Enerji bittiyse → durmalı
# - Yolu tıkandıysa → yeni rota hesaplamalı

# Bilgi al → karar ver → yol planla → uygulama → maliyet → sonuç kontrolü

# 1) Önce haritayı yap
# 2D grid
# engel/kaynak ekleme
# komşu kontrol fonksiyonu

# 2) Sonra robot sınıfını boş olarak oluştur
# Sadece:
# x, y
# energy

# 3) Strateji sınıflarını boş olarak ekle
# Her sınıfa sadece isim koy.

# 4) Pathfinding’i ekle (A veya BFS)*
# Test et → çalıştığından emin ol.

# 5) Robotun hareketini pathfinding’e bağla
# hedef seç
# yol bul
# hareket et

# 6) Enerji ve kaynak toplama ekle

# 7) Simülasyon döngüsünü bağla (main)

# 9) Sonradan Eklenebilecek Şeyler
# birden fazla strateji
# engellerin hareket etmesi
# görsel arayüz
# farklı robot türleri

# | Ne için?          | Kütüphane            |
# | ----------------- | -------------------- |
# | A* priority queue | `heapq`              |
# | Zaman gecikmesi   | `time` (opsiyonel)   |
# | Grafik            | `pygame` (opsiyonel) |

# 2D grid demek:
# Satırlar ve sütunlardan oluşan bir tablo
# Oyun haritaları, pathfinding haritaları hep böyle tutulur
# Python’da bu yapı list of lists ile yapılır
# Yani şöyle hayal et:

# Bu tablo:
# 0 → boş
# 1 → engel
# 2 → kaynak

# [ [0,0,0,0],
#   [0,1,0,2],
#   [0,0,0,0] ]

class Map:
  def __init__(self, width, height):
    self.width = width 
    self.height = height

    # def __init__(self):
    # self.width = 16
    # self.height = 16 
    # böyle olduğunda world = Map() yazabilirsin
    
    # 2D liste (harita) oluştur
    self.cells = []
    
    # --- 2D HARİTA OLUŞTURMA ---
    for y in range(height):  # her SATIR için
      row = []                     # yeni bir satır listesi oluştur
      for x in range(width): # her SÜTUN için
        row.append(0)              # 0 ekle (boş hücre)
      self.cells.append(row)         # satırı haritaya ekle

  def add_obstacle(self, x, y):
    if 0 <= y < self.height and 0 <= x < self.width:
      self.cells[y][x] = 1
  
  def add_resource(self, x, y):
    if 0 <= y < self.height and 0 <= x < self.width:
      self.cells[y][x] = 2

# cells = [[0 for x in range(width)] for y in range(height)]

world = Map(16, 16)  # sınıftan bir nesne oluştur
print(world.cells)   # o nesnenin içindeki 2D haritayı ekrana yaz

class Robot:
  def __init__(self, world, x, y, energy):
    self.world = world
    self.x = x
    self.y = y
    self.energy = energy
    self.dx = 0 
    self.dy = 0

  def check_cell(self):
      value = self.world.cells[self.y][self.x]
        # Eğer robotun altında “boş” varsa → value = 0
        # Engelse → value = 1
        # Kaynaksa → value = 2
      if value == 2:
        print("Kaynak bulundu, toplanıyor.")
        self.world.cells[self.y][self.x] = 0
        self.energy += 5
         # Robot hareket edince enerji harcıyor (-1)
         # Kaynak bulunca enerji kazanıyor (+5)
  
  # dx, dy PARAMETRE olarak alınmalı
  def move(self, dx, dy):
    # self.dx += dx  sildik
    # self.dy += dy  bu birikince çok hızlanır ve harita dışına çıkabilir, adım adım olduğu için sildik
    self.energy -= 1

    new_x = self.x + dx
    new_y = self.y + dy

     # sınır kontrolü
    if not (0 <= new_y < self.world.height and 0 <= new_x < self.world.width):
      print("Sınır dışı!")
      return

    if self.world.cells[new_y][new_x] == 1:
      print("Engel var.")
      return

    self.x = new_x
    self.y = new_y

robot1 = Robot(world, 0, 0, 100)
robot1.move(1, 0) # sağa 
robot1.move(0, 1) # aşağı

# Artık
# robot.x = 1
# robot.y = 1

print(robot1.x)
print(robot1.y)
print(robot1.energy)


    
    
    


# TEMİZ KOD --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Map:
  def __init__(self, width, height):
    self.width = width 
    self.height = height
  
    self.cells = []
    
    for y in range(height):  
      row = []                     
      for x in range(width): 
        row.append(0)             
      self.cells.append(row)         

  def add_obstacle(self, x, y):
    if 0 <= y < self.height and 0 <= x < self.width:
      self.cells[y][x] = 1

  def add_resource(self, x, y):
    if 0 <= y < self.height and 0 <= x < self.width:
      self.cells[y][x] = 2

world = Map(16, 16)  
print(world.cells)   


class Robot:
  def __init__(self, world, x, y, energy):
    self.world = world
    self.x = x
    self.y = y
    self.energy = energy
    self.dx = 0 
    self.dy = 0

  def check_cell(self):
    value = self.world.cells[self.y][self.x]
    if value == 2:
      print("Kaynak bulundu, toplanıyor.")
      self.world.cells[self.y][self.x] = 0
      self.energy += 5
  
  def move_dxdy(self, dx, dy):
    self.energy -= 1

    new_x = self.x + dx
    new_y = self.y + dy
     
    if not (0 <= new_y < self.world.height and 0 <= new_x < self.world.width):
      print("Sınır dışı!")
      return

    if self.world.cells[new_y][new_x] == 1:
      print("Engel var.")
      return

    self.x = new_x
    self.y = new_y

    self.check_cell()

  def look_cell(self, direction):
    dx = 0
    dy = 0
    
    if direction  == "right":
      dx = 1
    elif direction == "left":
      dx = -1
    elif direction == "up":
      dy = -1
    elif direction == "down":
      dy = 1

    # liste[0] → üst
    # liste[1] → orta
    # liste[2] → alt
    # bu yüzden yukarı cıktıkca azalır -1 

    new_x = self.x + dx
    new_y = self.y + dy
 
    if (0 <= new_y < self.world.height and 0 <= new_x < self.world.width): 
      value = self.world.cells[new_y][new_x]
      if value == 0:
        return "boş"
      elif value == 1:
        return "engel"
      elif value == 2:
        return "kaynak"
    else:
      return "sınır dışı"

  def move(self, direction):
    result = self.look_cell(direction)

    if result == "engel" or result == "sınır dışı":
      print("Hareket Edemem: ", result)
      return

    if direction == "right":
      dx = 1
    elif direction == "left":
      dx = -1
    elif direction == "up":
      dy = -1
    elif direction == "down":
      dy = 1

    self.move_dxdy(dx,dy)


world.add_resource(1,1)
world.add_obstacle(2,0)
world.add_obstacle(3,0)

robot1 = Robot(world, 0, 0, 100)
robot1.move(1, 0) # (1,0) - boş, hareket etmeli
print(robot1.x, robot1.y, robot1.energy)
robot1.move(0, 1) # (1,1) - engel var, hareket etmeyecek
print(robot1.x, robot1.y, robot1.energy)
robot1.move(1,0) # (2,1) - boş, hareket etmeli
print(robot1.x, robot1.y, robot1.energy)

  
  
        
      















