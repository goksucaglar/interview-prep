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

