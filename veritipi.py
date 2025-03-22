# Kullanıcıdan adını, yaşını ve doğum yılını alma
Ad = input("Adınızı girin: ")
Yaş = int(input("Yaşınızı girin: "))
Doğum_Yılı = int(input("Doğum yılınızı girin: "))

# Bilgileri ekrana yazdırma
print(f"Merhaba {Ad}! {Yaş} yaşındasın ve {Doğum_Yılı} yılında doğmuşsun.")

# Kullanıcıdan iki sayı alma
sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

# Dört işlem hesaplamaları ve ekrana yazdırma
toplam = sayi1 + sayi2
fark = sayi1 - sayi2
çarpım = sayi1 * sayi2
bölüm = sayi1 / sayi2 if sayi2 != 0 else "Tanımsız (0'a bölme)"

print(f"Toplam: {toplam}")
print(f"Fark: {fark}")
print(f"Çarpım: {çarpım}")
print(f"Bölüm: {bölüm}")

