# -*- coding: utf-8 -*-
"""prime_number_range.ipynb

Asal Sayı Aralığı: İki sayı arasındaki tüm asal sayıları bulan program        
Prime Number Range: A program that finds all prime numbers between two numbers
"""

start = int(input("Başlangıç sayısı: "))
end = int(input("Bitiş sayısı: "))

print("\nAsal sayılar:")
for num in range(start, end + 1):
    if num < 2:
        continue

    asal = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            asal = False
            break

    if asal:
        print(num, end=" ")

"""**fonksiyon ile yaparsak**

Bir sayının asal olup olmadığını kontrol etmek için:  2'den sadece √n’e kadar kontrol etmek yeterlidir.  Karekökü geçtiğin anda çarpanlar sadece tekrar etmeye başlar.      
49 asal mı?    
√49 = 7     
Kontrol et:     
2, 3, 4, 5, 6, 7 → 7’ye kadar kontrol yeter     
7’de tam bölünür → asal değildir
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

start = int(input("Başlangıç sayısı: "))
end = int(input("Bitiş sayısı: "))

print("\nAsal sayılar:")
for num in range(start, end + 1):
    if is_prime(num):
        print(num, end=" ")
