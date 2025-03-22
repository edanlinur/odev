# Kullanıcının girdiği bir sayının tek mi çift mi olduğunu kontrol etme
sayı=int(input("Bir sayı giriniz: "))
if sayı %2==0:
    print("Girdiğiniz sayı çifttir.")
else:
    print("Girdiğiniz sayı tektir.")

#Kullanıcının notunu alarak harf notu hesaplama
Notu= int(input("Notunuzu giriniz: "))
if 90 <= Notu <= 100:
    harf_notu = "A"
elif 80 <= Notu < 90:
    harf_notu = "B"
elif 70 <= Notu < 80:
    harf_notu = "C"
elif 60 <= Notu < 70:
    harf_notu = "D"
else:
    harf_notu = "F"

print(f"Harf notunuz: {harf_notu}")

# Kullanıcının yaşına göre yaş grubunu belirleme
yaş=int(input("Yaşınızı girin: "))
if yaş <= 12:
    yas_grubu = "Çocuk"
elif 13 <= yaş <= 19:
    yas_grubu = "Genç"
elif 20 <= yaş <= 59:
    yas_grubu = "Yetişkin"
else:
    yas_grubu = "Yaşlı"

print(f"Yaş grubunuz: {yas_grubu}")