# Kullanıcıdan 5 sayı alarak bir listeye ekleyen ve analiz eden program

numbers = []  # Sayıları saklayacak liste

for i in range(5):
    num = float(input(f"{i+1}. sayıyı girin: "))  # Kullanıcıdan sayı al
    numbers.append(num)

# Liste işlemleri
toplam = sum(numbers)
ortalama = toplam / len(numbers)
en_buyuk = max(numbers)
en_kucuk = min(numbers)

# Sonuçları yazdırma
print(f"Girilen Sayılar: {numbers}")
print(f"Toplam: {toplam}")
print(f"Ortalama: {ortalama}")
print(f"En Büyük Sayı: {en_buyuk}")
print(f"En Küçük Sayı: {en_kucuk}")

# Kullanıcıdan kelimeler alarak ters sırada yazdıran program

kelimeler = []  # Kelimeleri saklamak için liste

adet = int(input("Kaç kelime gireceksiniz? "))

for i in range(adet):
    kelime = input(f"{i+1}. kelimeyi girin: ")
    kelimeler.append(kelime)

# Listeyi ters çevirme
kelimeler.reverse()

print("Ters sıralanmış liste:", kelimeler)

# Tekrar eden elemanları kaldıran program

liste = [1, 2, 3, 4, 2, 3, 5, 6, 1, 7, 8, 5]
benzersiz_liste = list(set(liste))  # Set ile tekrar edenleri kaldırıp listeye çeviriyoruz

print("Tekrarsız Liste:", benzersiz_liste)