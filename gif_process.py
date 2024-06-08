from PIL import Image
import os
import re

# GIF dosyasını yükle
gif_dosyasi = 'turtle.gif'

# Frames klasörünü oluştur
if not os.path.exists('frames'):
    os.makedirs('frames')

# GIF'i aç ve her bir frame'i kaydet
with Image.open(gif_dosyasi) as img:
    for frame in range(0, img.n_frames):
        img.seek(frame)
        img.save(f'frames/frame_{frame}.gif')



# Frames klasöründeki dosya isimlerini listele
frame_listesi = os.listdir('frames')

# Sadece .gif uzantılı dosyaları filtrele
frame_listesi = [dosya for dosya in frame_listesi if dosya.endswith('.gif')]

# Dosya isimlerindeki sayıları çıkar
frame_numaralari = [int(re.search(r'\d+', dosya).group()) for dosya in frame_listesi]

# Sayılara göre sırala ve orijinal dosya isimlerini bu sıraya göre yeniden düzenle
frame_list = [x for _, x in sorted(zip(frame_numaralari, frame_listesi))]



