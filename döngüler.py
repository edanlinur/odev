#1’den 100’e kadar olan sayıları ekrana yazdırma
for i in range (1,101):
    print(i)

#1’den 100’e kadar sadece çift sayıları ekrana yazdıran bir program 
for i in range (2,101,2):
    print(i)

#Kullanıcıdan bir sayı alıp, bu sayının faktöriyelini hesaplayan bir program 
num = int(input("Faktöriyelini hesaplamak için bir sayı girin: "))

# Faktöriyel hesaplama
factorial = 1
if num < 0:
    print("Negatif sayıların faktöriyeli hesaplanamaz!")
elif num == 0 or num == 1:
    print(f"{num}! = 1")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"{num}! = {factorial}")
    
#1’den 100’e kadar olan tüm asal sayıları bulan bir program
print("1'den 100'e kadar olan asal sayılar:")

for num in range(2, 101):  # 1 asal sayı olmadığı için 2'den başlıyoruz
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):  # Sayının kareköküne kadar kontrol ediyoruz
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
print()
