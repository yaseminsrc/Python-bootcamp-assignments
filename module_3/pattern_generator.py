# -*- coding: utf-8 -*-
"""pattern_generator.ipynb

Desen Oluşturucu: Kullanıcının seçtiği deseni çizen program     
Pattern Generator: A program that draws the pattern selected by the user
"""

print("Desen Seç:\n1) Üçgen\n2) Piramit\n3) Ters üçgen")
choice = int(input("Seçim: "))
n = int(input("Yükseklik: "))

if choice == 1:
    for i in range(1, n + 1):
        print("*" * i)

elif choice == 2:
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2*i - 1))

elif choice == 3:
    for i in range(n, 0, -1):
        print("*" * i)

else:
    print("Geçersiz seçim!")

"""**fonksiyon ile yaparsak**"""

def dolu_ucgen(n, ch):
    for i in range(1, n + 1):
        print(ch * i)

def dolu_piramit(n, ch):
    for i in range(1, n + 1):
        print(" " * (n - i) + ch * (2 * i - 1))

def ters_ucgen(n, ch):
    for i in range(n, 0, -1):
        print(ch * i)

def ici_bos_piramit(n, ch):
    for i in range(1, n + 1):
        if i == 1:
            print(" " * (n - i) + ch)
        elif i == n:
            print(ch * (2 * n - 1))
        else:
            print(" " * (n - i) + ch + " " * (2 * i - 3) + ch)


print("Desen Seç:")
print("1) Dolu Üçgen")
print("2) Dolu Piramit")
print("3) Ters Üçgen")
print("4) İçi Boş Piramit")

secim = int(input("Seçim: "))
n = int(input("Yükseklik: "))
ch = input("Kullanılacak karakter: ")

if len(ch) != 1:
    print("Lütfen tek karakter girin!")
else:
    if secim == 1:
        dolu_ucgen(n, ch)
    elif secim == 2:
        dolu_piramit(n, ch)
    elif secim == 3:
        ters_ucgen(n, ch)
    elif secim == 4:
        ici_bos_piramit(n, ch)
    else:
        print("Geçersiz seçim!")
