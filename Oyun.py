import pygame
import math
import sys
import random
import time
import os

pygame.init()

# Ekran
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Futbol Oyunu")
clock = pygame.time.Clock()

# Renkler
WHITE = (230, 230, 230)
BLACK = (0, 0, 0)
RED = (200, 50, 50)
GREEN = (50, 200, 100)

# Karakter
eni, boyu = 64, 64
vel = 5

animasyon_zamanlayici = 0
frame_gecikmesi = 7

# Top
top_start = [150, HEIGHT - 50]
top_pos = list(top_start)
top_yaricap = 25
top_aci = 45
guc = 20
top_hareketli_mi = False
vektor = [0, 0]
yer_cekimi = 0.5
skor = 0
total_atislar = 0
sekme = 0
sekme_limiti = 3
sekmedeki_yukseklik_azalmasi = 0.7
top_donus_acisi = 0

# Şut animasyonu kontrol
sut_animation = False
sut_frame = 0

# Fontlar
font = pygame.font.SysFont(None, 28)
baslik_font = pygame.font.SysFont(None, 64)
skor_font = pygame.font.SysFont(None, 48)
skor_font = pygame.font.SysFont(None, 48)

def yuksek_skor_yukle():
    if os.path.exists("highest_score.txt"):
        with open("../../Desktop/highest_score.txt", "r") as f:
            return int(f.read())
    return 0

def yuksek_skor_kaydet(skor):
    with open("../../Desktop/highest_score.txt", "w") as f:
        f.write(str(skor))

yuksek_skor = yuksek_skor_yukle()
