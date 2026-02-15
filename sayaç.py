import time

sayi = int(input("Kaçtan geri sayılsın? "))

for i in range(sayi, 0, -1):
    print(i)
    time.sleep(1)  # 1 saniye bekler
print("Bitti!")