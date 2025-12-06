# -*- coding: utf-8 -*-
"""
Basit Dönüştürücü: Metre-Feet, Kilogram-Pound dönüştürücüsü yapın     
Simple Converter: Convert Meters to Feet, Kilograms to Pounds     
        ✔ 1 meter = 3.28084 feet    
        ✔ 1 kilogram = 2.20462 pound
"""
metre = float(input("Metre değeri: "))
feet = metre * 3.28084

print(f"{metre} metre = {feet:.2f} feet")

kg = float(input("Kilogram değeri: "))
pound = kg * 2.20462

print(f"{kg} kilogram = {pound:.2f} pound'dur")


# if-elif ile yaparsak
print("1 : Metre -> Feet")
print("2 : Feet -> Metre")
print("3 : Kilogram -> Pound")
print("4 : Pound -> Kilogram")

seçim = int(input("Seçiminiz : "))

if seçim ==1:
  metre = float(input("Metre: "))
  print("Feet: ", metre * 3.28084)

elif seçim ==2:
  feet = float(input("Feet: "))
  print("Metre: ", feet / 3.28084)

elif seçim ==3:
  kg = float(input("Kilogram: "))
  print("Pound: ", kg * 2.20462)

elif seçim ==4:
  pound = float(input("Pound: "))
  print("Kilogram: ", pound / 2.20462)
        

# Fonksiyon ile yaparsak
def dönüştür():
  print("1- Metre → Feet\n2- Feet → Metre\n3- Kilogram → Pound\n4- Pound → Kilogram")
  seçim = int(input("Seçiminiz: "))

  if seçim ==1:
    metre = float(input("Metre: "))
    print("Feet: ", metre * 3.28084)

  elif seçim ==2:
    feet = float(input("Feet: "))
    print("Metre: ", feet / 3.28084)

  elif seçim ==3:
    kg = float(input("Kilogram: "))
    print("Pound: ", kg * 2.20462)

  elif seçim ==4:
    pound = float(input("Pound: "))
    print("Kilogram: ", pound / 2.20462)

  else:
    print("Hatalı seçim yaptınız!")

dönüştür()
