# -*- coding: utf-8 -*-
"""passing_system.ipynb

Sınıf Geçme Sistemi: Kullanıcıdan notları alıp sınıf geçip geçmediğini, harf notunu gösteren program   
Passing System: A program that collects grades from the user and displays the letter grade for each grade.
"""

notu = float(input("Notunuzu girin (0-100): "))

if not 0 <= notu <= 100:
  print("Hata: Not 0-100 aralığında olmalı!")

else:
  if notu >= 90:
    harf = "AA"
  elif notu >= 85:
   harf = "BA"
  elif notu >= 80:
    harf = "BB"
  elif notu >= 70:
    harf = "CB"
  elif notu >= 60:
   harf = "CC"
  elif notu >= 50:
    harf = "DC"
  else:
    harf = "FF"

  durum = "Geçtiniz" if notu >= 50 else "Kaldınız"
  print("Harf Notu:", harf)
  print("Durum:", durum)

"""**fonksiyon ile yaparsak**"""

def passingSystem(grade):
    if not 0 <= grade <= 100:
        print("Error: Grade must be between 0-100!")
        return  # Fonksiyon burada durur o yüzden else bloğunda notları yazmaya gerek yok

    if grade >= 90:
        letter = "AA"
    elif grade >= 85:
        letter = "BA"
    elif grade >= 80:
        letter = "BB"
    elif grade >= 70:
        letter = "CB"
    elif grade >= 60:
        letter = "CC"
    elif grade >= 50:
        letter = "DC"
    else:
        letter = "FF"

    status = "Passed" if grade >= 50 else "Failed"
    return letter, status


grade = float(input("Enter your grade between (0-100): "))
result = passingSystem(grade)
if result:  # sonuc None değilse
    letter, status = result
    print("Letter Range:", letter)
    print("Status:", status)

"""**midterm (vize) %40,    final %60 alırsak**"""

vize = float(input("Vize notu: "))
final = float(input("Final notu: "))

ortalama = vize * 0.4 + final * 0.6
print(f"Ortalama: {ortalama}")

# Harf notu hesaplama
if ortalama >= 90:
    aralik = "AA"
elif ortalama >= 85:
    aralik = "BA"
elif ortalama >= 80:
    aralik = "BB"
elif ortalama >= 70:
    aralik = "CB"
elif ortalama >= 60:
    aralik = "CC"
elif ortalama >= 50:
    aralik = "DC"
else:
    aralik = "FF"

durum = "Geçti" if ortalama >= 50 else "Kaldı"

print(f"Harf Notu: {aralik}")
print(f"Durum: {durum}")

"""**fonksiyon ile yaparsak**"""

def sinif_gecme(v, f):
    ortalama = v * 0.4 + f * 0.6

    if ortalama >= 90:
        h = "AA"
    elif ortalama >= 85:
        h = "BA"
    elif ortalama >= 80:
        h = "BB"
    elif ortalama >= 70:
        h = "CB"
    elif ortalama >= 60:
        h = "CC"
    elif ortalama >= 50:
        h = "DC"
    else:
        h = "FF"

    drm = "Geçti" if ortalama >= 50 else "Kaldı"

    return ortalama, h, drm


v = float(input("Vize: "))
f = float(input("Final: "))

ortalama, h, drm = sinif_gecme(v, f)
print("Ortalama:", ortalama)
print("Harf:", h)
print("Durum:", drm)
