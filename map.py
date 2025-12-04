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
  width = 16
  heigth = 16

















