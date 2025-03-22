def hesap_makinesi(a, b):
    toplam = a + b
    fark = a - b
    carpim = a * b
    bolum = a / b if b != 0 else "Tanımsız"  # Bölme işleminde sıfıra bölmeyi önlüyoruz

    return toplam, fark, carpim, bolum

# Kullanıcıdan iki sayı al
sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

# Fonksiyonu çağır ve sonuçları yazdır
t, f, c, b = hesap_makinesi(sayi1, sayi2)
print(f"Toplam: {t}, Fark: {f}, Çarpım: {c}, Bölüm: {b}")


def palindrom_mu(kelime):
    kelime = kelime.lower().replace(" ", "")  # Küçük harfe çevirip boşlukları kaldırıyoruz
    return kelime == kelime[::-1]  # Kelimeyi ters çevirerek karşılaştırıyoruz

# Kullanıcıdan kelime al
kelime = input("Bir kelime girin: ")

# Sonucu ekrana yazdır
if palindrom_mu(kelime):
    print(f"'{kelime}' bir palindromdur.")
else:
    print(f"'{kelime}' bir palindrom değildir.")

def kac_yil_sonra_100_yas(yas):
    kalan_yil = 100 - yas
    return kalan_yil if kalan_yil > 0 else "Zaten 100 yaşını geçtiniz!"

# Kullanıcıdan yaş al
yas = int(input("Yaşınızı girin: "))

# Hesaplayıp sonucu yazdır
sonuc = kac_yil_sonra_100_yas(yas)
print(f"100 yaşına {sonuc} yıl sonra ulaşacaksınız.")