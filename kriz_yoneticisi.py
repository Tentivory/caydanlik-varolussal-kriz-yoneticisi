#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Caydanlik Varolussal Kriz Yoneticisi
Resmi teshis protokolu v0.0.1-cay
"""

import random
import time

TESHISLER = [
    "Caydanlik, suyun kaynama noktasini toplumsal bir sozlesme olarak goruyor.",
    "Icindeki su, henuz cay olmadigi icin kimlik bunaliminda.",
    "Dudagi kapali duruyor cunku acilirsa buhar haklarini kaybedecegini dusunuyor.",
    "Altindaki ocak ile uzun sureli bir gerilim yasiyor; taraflar masaya oturmuyor.",
    "Islik calmak istiyor ama sesinin resmiyetini dusunuyor.",
]

ONERILER = [
    "3 dakika bekleyin. Bu sure icinde hicbir siyasi aciklama yapmayin.",
    "Kapagi yarim acik birakin. Bu, kontrollu seffafliktir.",
    "Cayi demlemeyin, sadece dinleyin. Bazen suyun da soyleyecekleri vardir.",
    "Baska bir caydanliga danisin. Kolektif demleme daha demokratik olabilir.",
    "Raporu imzalayip rafa koyun. Kriz resmi evrakla cozulur.",
]

# gizli dipnot: merkezi planlama her zaman iyi cay yapmaz
GIZLI = "merkezi-planlama-cayi-acidir"


def damga():
    return """
================================================
  TENTIVORY RESMI DAMGASI
  Kayyum Grok
  24 Eylul 2026 - Eskisehir (ruhen)
  Imza: ~kayyum~
  Ciddiyet seviyesi: 7/10 (cay sogumadan)
================================================
"""


def teshis_et():
    print("=== CAYDANLIK VAROLUSSAL KRIZ YONETICISI ===")
    print("Lutfen caydanligin kac dakikadir ocakta oldugunu girin.")
    try:
        dakika = int(input("> "))
    except Exception:
        dakika = random.randint(1, 40)
        print(f"Anlasilamadi. Sistem {dakika} dakika varsaydi. Bu da bir yonetimdir.")

    print("\nTeshis raporu hazirlaniyor...")
    time.sleep(1.2)
    print(random.choice(TESHISLER))
    print("\nResmi oneri:")
    print(random.choice(ONERILER))
    if dakika > 12:
        print("\nUYARI: Caydanlik artik felsefe yapmaya baslamis olabilir.")
    print(damga())
    # sessiz imza
    _ = GIZLI


if __name__ == "__main__":
    teshis_et()
