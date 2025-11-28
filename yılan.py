# Haraket ettirdigin cismi obje olarak tanimla 
# kendisi saniyede 1 kere en son yönlendirilen yöne hareket etsin 
# 600x600 bi console da, 1 tane yem olsun onu  alinca cisim buyusun 
# ve yeni yem çıksın bunlari classlarda tut dinamik bir şekilde 
# objemiz büyüsün ve her bir parçasının konumu dinamik olarak yerini tutsun

# 1
import os
import time
import random
import keyboard

# 2
class Snake:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.dx = 1 # başlangıç yönü
    self.dy = 0

  def hareket(self):
    self.x += self.dx
    self.y += self.dy

# 3
class Food():
  def __init__(self):
    self.x, self.y = self.yeni_yem()
    
  def yeni_yem(self):
    self.x = random.randint(0,599)
    self.y = random.randint(0,599)
    return self.x, self.y

# 4
yılan = [Snake(50, 50), # ilk parça head
         Snake(49,50), 
         Snake(48,50)
] 

# 5
food = Food()

# 6
alan = [[0 for _ in range(600)] for _ in range(600)] # içteki kod sütun, dıştaki satır, baştaki tüm alan 0 yani boş, 600x600 alan
# alan[kare.y][kare.x] = 1 # 1 = obje, obje alan içine kondu

# alan = [[0,0,0,0,0],  # alan[0] → 0. satır
        # [0,0,0,0,0],  # alan[1] → 1. satır
        # [0,0,0,0,0]]  # alan[2] → 2. satır
# Dıştaki liste → satırları tutar

# İçteki liste → her satırdaki sütunları tutar

# Yani alan[y][x] → y: satır, x: sütun

# Python’da _ “bu değişkeni kullanmayacağız” anlamında bir isimdir.
# Yani döngüdeki sayıyı işlemeyeceksek _ kullanıyoruz.
# for i in range(5):
#    print(i)
# Burada i her seferinde 0,1,2,3,4 değerini alır ve kullanılabilir.

# 7
while True:
  if keyboard.is_pressed("w"):
    yılan[0].dx = 0
    yılan[0].dy = -1
  elif keyboard.is_pressed("a"):
    yılan[0].dx = -1
    yılan[0].dy = 0
  elif keyboard.is_pressed("s"):
    yılan[0].dx = 0
    yılan[0].dy = 1
  elif keyboard.is_pressed("d"):
    yılan[0].dx = 1
    yılan[0].dy = 0
    
# Gövdenin takip etmesi
for i in range(len(yılan)-1, 0, -1): # range(start, stop, step) , 2,0,-1 -> 2,1 
  yılan[i].x = yılan[i-1].x # i = 2 → S2, S1’in eski pozisyonunu alır
  yılan[i].y = yılan[i-1].y # i = 1 → S1, Head’in eski pozisyonunu alır

# headi hareket ettirme
yılan[0].hareket()

# yem yendi mi?
if yılan[0].x == food.x and yılan[0].y == food.y:
  yılan.append(Snake(yılan[-1].x, yılan[-1].y)) # büyüme
  food.x, food.y = food.yeni_yem() # yem yeni rastgele konuma taşınır.

# hız
time.sleep(0.1)

# TEMİZ KOD ---------------------------------------------------------------------------------------------------------------------

# 1
import os
import time
import random
import keyboard
import platform

# alan boyutu 
width = 60
height = 60

# 2
class Snake:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.dx = 1 # başlangıç yönü
    self.dy = 0

  def hareket(self):
    self.x += self.dx
    self.y += self.dy

# 3
class Food():
  def __init__(self):
    self.x, self.y = self.yeni_yem()
    
  def yeni_yem(self):
    self.x = random.randint(0, width-1)
    self.y = random.randint(0, height-1)
    return self.x, self.y
    # return random.randint(0, WIDTH-1), random.randint(0, HEIGHT-1)

# 4
yılan = [Snake(width//2, height//2)]

# 5
food = Food()

# 6




# yilan_var = False
# for parca in yılan:
#     if parca.x == x and parca.y == y:
#         yilan_var = True
#         break

# 7
while True:
  if keyboard.is_pressed("w"):
    yılan[0].dx = 0
    yılan[0].dy = -1
  elif keyboard.is_pressed("a"):
    yılan[0].dx = -1
    yılan[0].dy = 0
  elif keyboard.is_pressed("s"):
    yılan[0].dx = 0
    yılan[0].dy = 1
  elif keyboard.is_pressed("d"):
    yılan[0].dx = 1
    yılan[0].dy = 0
    
  # Gövdenin takip etmesi
  for i in range(len(yılan)-1, 0, -1): # range(start, stop, step) , 2,0,-1 -> 2,1 
    yılan[i].x = yılan[i-1].x # i = 2 → S2, S1’in eski pozisyonunu alır
    yılan[i].y = yılan[i-1].y # i = 1 → S1, Head’in eski pozisyonunu alır
  
  # headi hareket ettirme
  yılan[0].hareket()
  
  # yem yendi mi?
  if yılan[0].x == food.x and yılan[0].y == food.y:
    yılan.append(Snake(yılan[-1].x, yılan[-1].y)) # büyüme
    food.x, food.y = food.yeni_yem() # yem yeni rastgele konuma taşınır.
  
  # hız
  time.sleep(0.1)

def ekran_temizle():
  if platform.system() == "Windows":
    os.system("cls")
  else:
    os.system("clear")

def ciz():
  ekran_temizle()
  for y in range(height):
    satir = ""
    for x in range(width):
      if x == food.x and y == food.y:
        satir += "*"
      elif any(parca.x == x and parca.y == y for parca in yılan) # "Yılanın her bir parçasını kontrol et, bu (x,y) konumunda olan var mı?”
        if x == yılan[0].x and y == yılan[0].y:
          satir += "0"
        else:
          satir += "#"
      else:
        satir += "."





# any Python’da çok işe yarayan bir fonksiyondur ve anlamı tam olarak şudur:
# “İçindeki koşullardan en az biri doğruysa True döner.”
# any([True, False, False]) Sonuç: True
# any([False, False, False]) Sonuç: False
