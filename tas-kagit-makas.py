#random bir şekilde taş kağit makas oyna
#kullanıcı 1-tas 2-kagit 3-makas girsin
#o sırada random bir şekilde bot oynasın 
#kimin kazandığını yazsın 

import random

print("1-Taş 2-Kağıt 3-Makas")
sayi = int(input("Sayı giriniz: "))

def tkm(sayi):
  if 1 <= sayi <= 3:
    kullanici = sayi
    bot = random.randint(1,3)
    print("Kullanıcı:", kullanici)
    print("Bot:", bot)
    if kullanici == bot:
      print("BERABERE")
    elif (kullanici == 1 and bot == 3) or (kullanici == 2 and bot == 1) or (kullanici == 3 and bot == 2):
        print("KAZANDINIZ")
    else:
        print("KAYBETTİNİZ")
    
tkm(sayi)

#------------------------------------------------------------------------------------------------------------
#daha iyi kod

import random

def tkm(sayi):
  kullanici = sayi
  bot = random.randint(1,3)

  secimler = {1: "Taş", 2: "Kağıt", 3: "Makas" }
  print("Kullanıcı:", secimler[kullanici])
  print("Bot:", secimler[bot])

  if kullanici == bot:
    print("Berabere!")
  elif (kullanici == 1 and bot == 3) or (kullanici == 2 and bot == 1) or (kullanici == 3 and bot == 2):
    print("Kazandınız!")
  else:
    print("Kaybettiniz!")

sayi = int(input("Sayı giriniz: "))
tkm(sayi)








