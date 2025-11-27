# Haraket ettirdigin cismi obje olarak tanimla 
# kendisi saniyede 1 kere en son yönlendirilen yöne hareket etsin 
# 600x600 bi console da, 1 tane yem olsun onu  alinca cisim buyusun 
# ve yeni yem çıksın bunlari classlarda tut dinamik bir şekilde 
# objemiz büyüsün ve her bir parçasının konumu dinamik olarak yerini tutsun

import os
import time
import random

class Obje:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def hareket(self):
    self.x += dx
    self.y += dy

kare = Obje(50, 50) # obje başlangıçta 50,50 koordinatında

# for y in range(600):
  # satır = [] # her satır için boş bir liste oluşturma
  # for x in range(600):
    # satir.append(0)
#  alan.append(satir)

alan = [[0 for _ in range(600)] for _ in range(600)] # içteki kod sütun, dıştaki satır, baştaki tüm alan 0 yani boş, 600x600 alan
alan[kare.y][kare.x] = 1 # 1 = obje, obje alan içine kondu

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

def yeni_yem():
  return random.randint(0,599), random.randint(0,599)

yem_x, yem_y = yeni_yem()
# yem_x → fonksiyondan dönen ilk değer (x koordinatı)
# yem_y → fonksiyondan dönen ikinci değer (y koordinatı)




