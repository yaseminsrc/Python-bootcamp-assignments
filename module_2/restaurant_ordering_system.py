# -*- coding: utf-8 -*-
"""restaurant_ordering_system.ipynb

Restoran Sipariş Sistemi: Menüden seçim yapıp toplam tutarı hesaplayan program    
Restaurant Ordering System: Program that makes selections from the menu and calculates the total amount
"""

menu = {
    "1": ("Pizza", 120),
    "2": ("Hamburger", 80),
    "3": ("Kola", 20),
    "4": ("Su", 10)
}

toplam = 0

print("---- MENÜ ----")
for k, v in menu.items():
    print(f"{k}) {v[0]} - {v[1]} TL")

while True:
    secim = input("Sipariş numarası (çıkmak için q): ")

    if secim == "q":
        break

    if secim in menu:
        toplam += menu[secim][1]
        print(f"{menu[secim][0]} eklendi. Güncel toplam: {toplam} TL")
    else:
        print("Geçersiz seçim!")

print(f"Toplam ödemeniz gereken tutar: {toplam} TL")

"""**fonksiyon ile yaparsak**

restoran_siparis fonksiyonu menüyü parametre olarak alıyor ve kullanıcıdan seçimleri topluyor.
Döngü içinde kullanıcı istediği kadar sipariş ekleyebilir, çıkmak için q yazabilir.
Fonksiyon toplam ödemeyi geri döndürüyor.
Menü değişirse veya yeni ürün eklenirse sadece menu sözlüğünü güncellemek yeterli.
"""

def restoran_siparis(menu):
    """
    Menüden seçim yapıp toplam tutarı hesaplayan fonksiyon.
    menu: {"1": ("Ürün Adı", Fiyat), ...}
    """
    toplam = 0
    print("---- MENÜ ----")
    for k, v in menu.items():
        print(f"{k}) {v[0]} - {v[1]} TL")

    while True:
        secim = input("Sipariş numarası (çıkmak için q): ")
        if secim == "q":
            break
        elif secim in menu:
            toplam += menu[secim][1]
            print(f"{menu[secim][0]} eklendi. Güncel toplam: {toplam} TL")
        else:
            print("Geçersiz seçim!")

    return toplam

# Menü tanımı
menu = {
    "1": ("Pizza", 120),
    "2": ("Hamburger", 80),
    "3": ("Kola", 20),
    "4": ("Su", 10)
}

# Fonksiyonu çağır
toplam_odeme = restoran_siparis(menu)
print(f"\nToplam ödemeniz gereken tutar: {toplam_odeme} TL")

"""**menü sipariş sistemini her ürünün kaç adet alındığını takip eden ve toplamı hesaplama**

Her ürün için kaç adet sipariş verildiğini saklıyor.
Toplam tutarı sürekli güncelliyor ve kullanıcıya gösteriyor.
Döngü sonunda sipariş detaylarını ve toplam ödemeyi gösteriyor.
Menüye yeni ürün eklemek çok kolay; sadece menu sözlüğünü güncellemek yeterli.
"""

def restoran_siparis_detayli(menu):
    """
    Menüden seçim yapıp toplam tutarı ve her ürünün adetini hesaplayan fonksiyon.
    menu: {"1": ("Ürün Adı", Fiyat), ...}
    """
    toplam = 0
    siparisler = {k: 0 for k in menu}  # Her ürünün sipariş adedi

    print("---- MENÜ ----")
    for k, v in menu.items():
        print(f"{k}) {v[0]} - {v[1]} TL")

    while True:
        secim = input("Sipariş numarası (çıkmak için q): ")
        if secim == "q":
            break
        elif secim in menu:
            siparisler[secim] += 1
            toplam += menu[secim][1]
            print(f"{menu[secim][0]} eklendi. Güncel toplam: {toplam} TL (Adet: {siparisler[secim]})")
        else:
            print("Geçersiz seçim!")

    # Sipariş detaylarını yazdır
    print("\n---- Sipariş Detayları ----")
    for k, adet in siparisler.items():
        if adet > 0:
            print(f"{menu[k][0]}: {adet} adet - {menu[k][1] * adet} TL")

    return toplam

# Menü tanımı
menu = {
    "1": ("Pizza", 120),
    "2": ("Hamburger", 80),
    "3": ("Kola", 20),
    "4": ("Su", 10)
}

# Fonksiyonu çağır
toplam_odeme = restoran_siparis_detayli(menu)
print(f"\nToplam ödemeniz gereken tutar: {toplam_odeme} TL")
