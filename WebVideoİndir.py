import yt_dlp

# İndirmek istediğin video URL'sini buraya yaz
url = input("URL GİR")

# İndirme ayarları
ydl_opts = {
    "outtmpl": "C:/Users/AZMAN/Desktop/%(title)s.%(ext)s",  # Masaüstüne kaydeder
    "format": "best"  # En iyi kaliteyi seçer
}

# Video indirme işlemi
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])