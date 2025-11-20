#random bir şekilde taş kağit makas oyna
#kullanıcı 1-tas 2-kagit 3-makas girsin
#o sırada random bir şekilde bot oynasın 
#kimin kazandığını yazsın 

import random

print("-----------------TAŞ-KAĞIT-MAKAS-----------------")
print(" ")
print("1-Taş 2-Kağıt 3-Makas")
print(" ")
sayi = int(input("Sayı giriniz: "))

def tkm(sayi):
  if 1 <= sayi <= 3:
    kullanici = sayi
    bot = random.randint(1,3)
    print("Kullanıcı:", kullanici)
    print("Bot:", bot)
    if kullanici == bot:
      print("SONUÇ: BERABERE")
    elif (kullanici == 1 and bot == 3) or (kullanici == 2 and bot == 1) or (kullanici == 3 and bot == 2):
        print("SONUÇ: KAZANDINIZ")
    else:
        print("SONUÇ: KAYBETTİNİZ")
    
tkm(sayi)

#düzeltilmiş hali-------------------------------------------------------------------------------------------

import random

print("-----------------TAŞ-KAĞIT-MAKAS-----------------")
print(" ")

sayi = int(input("Sayı giriniz: "))

secimler = { 1: "Taş", 2: "Kağıt", 3: "Makas" }

def tkm(sayi):
  if 1 <= sayi <= 3:
    kullanici = sayi
    bot = random.randint(1,3)
    print("Kullanıcı Seçimi: ", secimler[kullanici])
    print("Bot Seçimi: ", secimler[bot])
    if (kullanici == 1 and bot == 3) or (kullanici == 2 and bot == 1) or (kullanici == 3 and bot == 2):
      print("Sonuç: Kazandınız!")
    elif kullanici == bot:
      print("Sonuç: Berabere!")
    else:
      print("Sonuç: Kaybettiniz!")

tkm(sayi)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#daha iyi kod

import random

print("-----------------TAŞ-KAĞIT-MAKAS-----------------")
print(" ")

def tkm(sayi):
  kullanici = sayi
  bot = random.randint(1,3)

  secimler = {1: "Taş", 2: "Kağıt", 3: "Makas" }
  print("Kullanıcı:", secimler[kullanici])
  print("Bot:", secimler[bot])

  if kullanici == bot:
    print("Sonuç: Berabere!")
  elif (kullanici == 1 and bot == 3) or (kullanici == 2 and bot == 1) or (kullanici == 3 and bot == 2):
    print("Sonuç: Kazandınız!")
  else:
    print("Sonuç: Kaybettiniz!")

sayi = int(input("Sayı giriniz: "))
tkm(sayi)



#Bitiş 21.11.2025, 01.05, Cuma




