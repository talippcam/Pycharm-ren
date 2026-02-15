import yt_dlp

url = "https://www.youtube.com/watch?v=2EySphZzHCk"
ydl_opts = {"outtmpl": "C:/Users/AZMAN/Desktop/%(title)s.%(ext)s"}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])