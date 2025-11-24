# @ işaretini W, A, S, D ile hareket ettirme.
# import keyboard: klavyenin tüm kontrolünü ele geçiren bir (modül) kütüphanedir.
# Bu modülle istediğinizi yazabilir, kısayol tuşları oluşturabilir, kısaltmalar oluşturabilir, klavyeyi engelleyebilir, giriş bekleyebilir vb.
# keyboard.write(message, [delay]) - gecikmeli veya gecikmesiz bir mesaj yazar.
# keyboard.wait(key) - key tuşuna basılana kadar programı engeller. keyTuş, string ( 'space', 'esc' vb. ) olarak geçirilir. Bir tuşa basılmasını bekleme.   (*)
# keyboard.press(key)- Bir tuşa basar ve fonksiyon çağrılana kadar basılı tutar. release(key)
# keyboard.release(key) - bir anahtar serbest bırakır.
# keyboard.send(key) - bir tuşa basar ve bırakır.
# keyboard.add_hotkey(hotkey, function) - Python’daki keyboard kütüphanesinde bir kısayol tuşu (hotkey) atamak için kullanılır.    (*)
# keyboard.record(key) key - tuşuna basılana kadar klavye etkinliğini kaydeder.
# keyboard.play(recorded_events, [speed_factor]) - fonksiyonu ile kaydedilen olayları keyboard.record(key)isteğe bağlı olarak tekrar oynatır speed_factor.
# while True: Python’da sonsuz döngü oluşturur. İçine ne koyarsan program onu durmadan çalıştırır.
# Sonsuz döngüler CPU’yu yorabilir. Döngüye bir çıkış koşulu eklemek genelde daha iyidir.
# keyboard.is_pressed() fonksiyonu, Python’daki keyboard kütüphanesinde bir tuşun o anda basılı olup olmadığını kontrol eder.
# keyboard.wait('esc') Esc ile programı durdur.

while True:
  print("Çalışıyor...")
  if keyboard.is_pressed('esc'):  # esc tuşuna basılı
    print("Döngü sonlandırıldı.")
    break

# import keyboard
# from time import sleep
# time.sleep(0.1)

# press_and_release ile normal bir tuş vuruşu simüle etmiş oluruz.

import keyboard
import time

keyboard.press('up')
time.sleep(0.1)
keyboard.release('up')
keyboard.press_and_release('up')

# K O D -----------------------------------------------------------------------------------------------------------------------

import os # sistem komutları için gerekli 
import keyboard
import time
import shutil # terminal genişlik - yükseklik değerlerini almamız için lazım, asıl amacı dosya ve klasör işleme
import platform # işletim sistemini öğrenmek için kullanılır linux/mac mi windows mu ona bakmamızı sağlar

karakter = input("Karakterimiz: ")
x = 5 # dikey başlangıç 
y = 2 # yatay başlangıç (ilk önce satıra bak satır 0,satır 1 -> boş // satır 2 -> 5 boşluk + karakter çizilir)
# satir_sayisi = 20 # terminal yüksekliği yapabilirdik 
max_sag = shutil.get_terminal_size().columns - 1 # terminal genişliğini al ve sap sınırı belirle, şuanki boyutunu görür
max_alt = shutil.get_terminal_size().lines - 1
# çıktısı .columns ve .lines içerir. 
# pythonda indexler 0 dan başladığı için - 1

# boyut = shutil.get_terminal_size()
# print(boyut.columns)
# print(boyut.lines)

def yukari():
  global y # python içindeki bir fonksiyona dışardaki değişkeni çağırmak için global gerekir.
  y -= 1
  if y < 0: # karakter en üst satırdaysa -1 diye bir şey olmaz, üst sınır
    y = 0 
 
def asagi():
  global y
  y += 1
  # if y > satir_sayisi - 1: # karakterin ekranın altından dışarı çıkmasını engeller.
    # y = satir_sayisi - 1 # 0 dan 19 a kadar olduğu için, 20 - 1 = 19, range(20), alt sınır
  if y > max_alt:
    y = max_alt
    
def sag():
  global x 
  x += 1 # sağ tarafta bir sınır koymamız için terminalin uzunluğunu alacağız
  if x > max_sag: # sağ sınır
    x = max_sag

def sol():
  global x
  x -= 1
  if x < 0: # karakter en soldaysa 0 olur, sol sınır
    x = 0

def karakter_ciz(): # tüm satırları gezer 
  for i in range(max_alt + 1): # 0 dan başlıyor + 1 o yüzden, önce y yani hangi satırda olacağına bakıyoruz sonra x kadar sağa kaydır
    if i == y: # döngü satırı y konumuna eşitse
      print(" " * x + karakter) # x kadar boşluk + karakter, x kadar sağa kaydırıyoruz 
    else:
      print() # boş satır 

keyboard.add_hotkey('w', yukari)
keyboard.add_hotkey('s', asagi)
keyboard.add_hotkey('a', sol)
keyboard.add_hotkey('d', sag)

def ekran_temizle():
  if platform.system() == "Windows":
    os.system("cls")
  else: # linux ve mac
    os.system("clear")

while True: 
  # os.system("cls") # windows için ekranı temizle
  ekran_temizle()
  karakter_ciz() # karakteri yeni konumda çiz
  if keyboard.is_pressed('esc'): # esc ile çıkış
    break
  time.sleep(0.05) # cpu'yu yormamak için kısa bekleme

# TEMİZ KOD -----------------------------------------------------------

import os 
import keyboard
import time
import shutil 
import platform 

karakter = input("Karakterimiz: ")

x = 5 
y = 2 

max_sag = shutil.get_terminal_size().columns - 1 
max_alt = shutil.get_terminal_size().lines - 1

def yukari():
  global y 
  y -= 1
  if y < 0: 
    y = 0 
 
def asagi():
  global y
  y += 1
  if y > max_alt:
    y = max_alt
    
def sag():
  global x 
  x += 1 
  if x > max_sag: 
    x = max_sag

def sol():
  global x
  x -= 1
  if x < 0: 
    x = 0

def karakter_ciz(): 
  for i in range(max_alt + 1): 
    if i == y: 
      print(" " * x + karakter) 
    else:
      print() 
      
keyboard.add_hotkey('w', yukari)
keyboard.add_hotkey('s', asagi)
keyboard.add_hotkey('a', sol)
keyboard.add_hotkey('d', sag)

def ekran_temizle():
  if platform.system() == "Windows":
    os.system("cls")
  else: # linux ve mac
    os.system("clear")

while True: 
  ekran_temizle()
  karakter_ciz() 
  if keyboard.is_pressed('esc'): 
    break
  time.sleep(0.05) 
 
# Bitiş 25.11.2025, 02:00, Salı
  








