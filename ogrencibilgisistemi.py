#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  4 00:05:23 2025

@author: selenguven
"""
ogrenciler = []

def veri_yukle():
    try:
        with open("ogrenciler.txt", "r", encoding="utf-8") as dosya:
            for satir in dosya:
                isim, vize, final, ortalama, harf = satir.strip().split(",")
                ogrenci = {
                    "isim" : isim,
                    "vize_notu" : int(vize),
                    "final_notu" : int(final),
                    "ortalama": float(ortalama),
                    "harf": str(harf)
                }
                ogrenciler.append(ogrenci)
        print ("Kayıt başarıyla oluşturuldu.")
    except FileNotFoundError:
        print("Dosya yok , baştan başla.")

def obys():
    isim = input("Lütfen bir isim giriniz: ")
    vize_notu = int(input("Lütfen vize notunu giriniz: "))
    final_notu = int(input("Lütfen final notunu giriniz."))
    ogrenci = {"isim": isim, "vize_notu": vize_notu, "final_notu": final_notu}
    ogrenciler.append(ogrenci)
    print("\nÖğrenci Eklendi.")
    
def ogrenci_listele():
    if not ogrenciler:
        print("Henüz kayıtlı öğrenci yok.")
        return
    print("\n---Öğrenci Listesi---")
    for i, ogr in enumerate(ogrenciler):
        print(f"{i+1}. {ogr['isim']} -- Vize Notu: {ogr['vize_notu']} -- Final Notu: {ogr['final_notu']}")

def durum_hesapla():
    for ogr in ogrenciler:
        vize = ogr["vize_notu"]
        final = ogr["final_notu"]
        ortalama = vize * 0.4 + final * 0.6
        ogr["ortalama"] = ortalama
        print(f"{ogr['isim']} adlı öğrencinin ortalaması {ortalama}")
        
        if ortalama >= 90:
            harf = "AA"
        elif ortalama >= 80:
            harf = "BA"
        elif ortalama >= 75:
            harf = "BB"
        elif ortalama >= 70:
            harf = "CB"
        elif ortalama >= 60:
            harf = "CC"
        elif ortalama >= 50:
            harf = "DC"
        else:
            harf = "FF"
        ogr["harf"] = harf
        if ortalama >= 50:
            durum = "Geçti"
        else:
            durum = "Kaldı"
        print(f"{ogr['isim']} Harf Notu {harf} -- Durumu {durum}")

def not_guncelle():
    if not ogrenciler:
        print("Henüz kayıtlı öğrenci yok.")
        return
    ogrenci_listele()
    try:
        secim = int(input("Kaç numaralı öğrencinin notunu güncellemek istersiniz? ")) -1
        if secim < 0 or secim >= len(ogrenciler):
            print("Geçersiz sayı.")
            return
        
        yeni_vize_not = int(input("Güncellemek istediğiniz yeni vize notunu giriniz: "))
        yeni_final_not = int(input("Güncellemek istediğiniz yeni final notunu giriniz: "))
        ogrenciler[secim]["vize_notu"] = yeni_vize_not
        print("Vize notu güncellendi.")
        ogrenciler[secim]["final_notu"] = yeni_final_not
        print("Final notu güncellendi")
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz.")
  
def veri_kaydet():
    with open("ogrenciler.txt", "w", encoding="utf-8") as dosya:
        for ogr in ogrenciler:
            ortalama = ogr.get("ortalama" ,0)
            harf = ogr.get("harf", "hesaplanmadı")
            satir = f"{ogr['isim']},{ogr['vize_notu']},{ogr['final_notu']},{ogr['ortalama']},{ogr['harf']}\n"
            dosya.write(satir)
        print("Veriler dosyaya kaydedildi.")
        
def menu():
    veri_yukle()
    
    while True:
        print("\nÖğrenci Bilgi Sistemi (OBS)'ye Hoşgeldiniz")
        print("1. Not Gir")
        print("2. Not Güncelle")
        print("3. Ortalama ve Durum Gör")
        print("4. Öğrencileri Listele")
        print("5. Çıkış")
        
        secim = input("Seçiminiz: ")
        
        if secim == "1":
            obys()
        elif secim == "2":
            not_guncelle()
        elif secim == "3":
            durum_hesapla()
        elif secim == "4":
            ogrenci_listele()
        elif secim == "5":
            veri_kaydet()
            print("Güle Gülee")
            break
        else:
            print("Lütfen geçerli bir numara giriniz (1-5)")
        
menu()















