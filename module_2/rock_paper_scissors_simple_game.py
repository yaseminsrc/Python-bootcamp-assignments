# -*- coding: utf-8 -*-
"""rock_paper_scissors_simple_game.ipynb

Basit Oyun: Kullanıcı ile bilgisayarın taş-kağıt-makas oynadığı program     
Simple Game: A program where the user and the computer play rock-paper-scissors.
"""

import random

secenekler = ["taş", "kağıt", "makas"]

kullanici = input("Taş, kağıt veya makas seçin: ").lower()
bilgisayar = random.choice(secenekler)

print(f"Bilgisayar: {bilgisayar}")

if kullanici == bilgisayar:
    print("Berabere!")
elif (kullanici == "taş" and bilgisayar == "makas") or \
     (kullanici == "makas" and bilgisayar == "kağıt") or \
     (kullanici == "kağıt" and bilgisayar == "taş"):
    print("Kazandınız!")
else:
    print("Kaybettiniz!")

"""**fonksiyon ile yaparsak**

tas_kagit_makas() fonksiyonu tüm oyunu kapsıyor.
Kullanıcı seçim yapıyor, bilgisayar rastgele seçim yapıyor.
Sonuç karşılaştırılarak kazandı / kaybetti / berabere mesajı gösteriliyor.
Kullanıcı yanlış bir giriş yaparsa tekrar soruyor.
"""

import random

def tas_kagit_makas():
    """
    Taş-kağıt-makas oyunu oynatan fonksiyon.
    Kullanıcıdan seçim alır, bilgisayar rastgele seçim yapar ve sonucu yazdırır.
    """
    secenekler = ["taş", "kağıt", "makas"]

    kullanici = input("Taş, kağıt veya makas seçin: ").lower()
    while kullanici not in secenekler:
        print("Geçersiz seçim! Tekrar deneyin.")
        kullanici = input("Taş, kağıt veya makas seçin: ").lower()

    bilgisayar = random.choice(secenekler)
    print(f"Bilgisayar: {bilgisayar}")

    if kullanici == bilgisayar:
        print("Berabere!")
    elif (kullanici == "taş" and bilgisayar == "makas") or \
         (kullanici == "makas" and bilgisayar == "kağıt") or \
         (kullanici == "kağıt" and bilgisayar == "taş"):
        print("Kazandınız!")
    else:
        print("Kaybettiniz!")

# Oyunu başlat
tas_kagit_makas()

"""Taş-Kağıt-Makas oyununu birden fazla tur oynatan ve skor tutan ve kazananı gösteren fonksiyon hâline getirelim. Böylece kullanıcı ve bilgisayarın kazandığı tur sayısını takip edip, oyunun sonunda kazananı görebileceğiz.

Birden fazla tur oynanabilir (varsayılan 3, parametreyle değiştirilebilir).
Skor takibi var: kullanıcı ve bilgisayarın kazandığı turlar ayrı ayrı sayılıyor.
Her tur sonunda güncel skor gösteriliyor.
Oyun sonunda genel kazanan açıklanıyor.
"""

import random

def tas_kagit_makas_oyna(tur_sayisi=3):
    """
    Çok turlu taş-kağıt-makas oyunu.
    Kullanıcı ve bilgisayarın skorunu tutar ve sonunda kazananı gösterir.
    tur_sayisi: kaç tur oynanacağını belirler (varsayılan 3 tur)
    """
    secenekler = ["taş", "kağıt", "makas"]
    skor_kullanici = 0
    skor_bilgisayar = 0

    for tur in range(1, tur_sayisi + 1):
        print(f"\n--- Tur {tur} ---")
        kullanici = input("Taş, kağıt veya makas seçin: ").lower()
        while kullanici not in secenekler:
            print("Geçersiz seçim! Tekrar deneyin.")
            kullanici = input("Taş, kağıt veya makas seçin: ").lower()

        bilgisayar = random.choice(secenekler)
        print(f"Bilgisayar: {bilgisayar}")

        if kullanici == bilgisayar:
            print("Berabere!")
        elif (kullanici == "taş" and bilgisayar == "makas") or \
             (kullanici == "makas" and bilgisayar == "kağıt") or \
             (kullanici == "kağıt" and bilgisayar == "taş"):
            print("Kazandınız bu turu!")
            skor_kullanici += 1
        else:
            print("Bilgisayar kazandı bu turu!")
            skor_bilgisayar += 1

        print(f"Skor: Siz {skor_kullanici} - Bilgisayar {skor_bilgisayar}")

    # Oyunun sonucu
    print("\n--- Oyun Bitti ---")
    if skor_kullanici > skor_bilgisayar:
        print(f"Tebrikler! Oyunu {skor_kullanici} - {skor_bilgisayar} skorla kazandınız.")
    elif skor_bilgisayar > skor_kullanici:
        print(f"Üzgünüz! Oyunu {skor_bilgisayar} - {skor_kullanici} skorla bilgisayar kazandı.")
    else:
        print(f"Oyun berabere! Skor: {skor_kullanici} - {skor_bilgisayar}")

# Oyunu başlat (örnek: 5 tur)
tas_kagit_makas_oyna(tur_sayisi=5)

"""Taş-Kağıt-Makas oyununu kullanıcı isterse tekrar oynayabileceği şekilde geliştirirsek böylece oyun bittiğinde kullanıcı “tekrar oynamak istiyor musunuz?” sorusuna cevap verebilir ve oyuna baştan başlayabilir.

Kullanıcı kaç tur oynayacağını seçebilir (varsayılan 3 tur).
Oyunun sonunda skor ve kazanan gösterilir.
Kullanıcı isterse oyunu tekrar başlatabilir.
Döngü ile oyun istediğiniz kadar tekrar oynanabilir.
"""

import random

def tas_kagit_makas_oyna(tur_sayisi=3):
    """
    Çok turlu taş-kağıt-makas oyunu.
    Kullanıcı ve bilgisayarın skorunu tutar ve sonunda kazananı gösterir.
    tur_sayisi: kaç tur oynanacağını belirler (varsayılan 3 tur)
    """
    secenekler = ["taş", "kağıt", "makas"]
    skor_kullanici = 0
    skor_bilgisayar = 0

    for tur in range(1, tur_sayisi + 1):
        print(f"\n--- Tur {tur} ---")
        kullanici = input("Taş, kağıt veya makas seçin: ").lower()
        while kullanici not in secenekler:
            print("Geçersiz seçim! Tekrar deneyin.")
            kullanici = input("Taş, kağıt veya makas seçin: ").lower()

        bilgisayar = random.choice(secenekler)
        print(f"Bilgisayar: {bilgisayar}")

        if kullanici == bilgisayar:
            print("Berabere!")
        elif (kullanici == "taş" and bilgisayar == "makas") or \
             (kullanici == "makas" and bilgisayar == "kağıt") or \
             (kullanici == "kağıt" and bilgisayar == "taş"):
            print("Kazandınız bu turu!")
            skor_kullanici += 1
        else:
            print("Bilgisayar kazandı bu turu!")
            skor_bilgisayar += 1

        print(f"Skor: Siz {skor_kullanici} - Bilgisayar {skor_bilgisayar}")

    # Oyunun sonucu
    print("\n--- Oyun Bitti ---")
    if skor_kullanici > skor_bilgisayar:
        print(f"Tebrikler! Oyunu {skor_kullanici} - {skor_bilgisayar} skorla kazandınız.")
    elif skor_bilgisayar > skor_kullanici:
        print(f"Üzgünüz! Oyunu {skor_bilgisayar} - {skor_kullanici} skorla bilgisayar kazandı.")
    else:
        print(f"Oyun berabere! Skor: {skor_kullanici} - {skor_bilgisayar}")

# Ana döngü: kullanıcı isterse tekrar oynasın
while True:
    tur_sayisi = input("Kaç tur oynamak istersiniz? (Varsayılan 3): ")
    tur_sayisi = int(tur_sayisi) if tur_sayisi.isdigit() else 3
    tas_kagit_makas_oyna(tur_sayisi=tur_sayisi)

    tekrar = input("\nTekrar oynamak ister misiniz? (e/h): ").lower()
    if tekrar != 'e':
        print("Oyun kapatılıyor. Teşekkürler!")
        break
