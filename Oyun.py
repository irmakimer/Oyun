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

# Menü
menu = True
oyun_bitti = False
start_time = None
zaman_siniri = 90
gecen_sure = 0

# Random kale yeri ve boyutu
def random_hoop():
    hoop_y = random.randint(100, HEIGHT - 200)
    hoop_h = random.randint(80, 140)
    return pygame.Rect(WIDTH - 120, hoop_y, 100, hoop_h)

def yuksek_skor_yukle():
    if os.path.exists("highest_score.txt"):
        with open("../../Desktop/highest_score.txt", "r") as f:
            return int(f.read())
    return 0

def yuksek_skor_kaydet(skor):
    with open("../../Desktop/highest_score.txt", "w") as f:
        f.write(str(skor))

yuksek_skor = yuksek_skor_yukle()
hoop = random_hoop()

def reset_top():
    global top_pos, vektor, top_hareketli_mi, sekme, top_donus_acisi
    top_pos = list(top_start)
    vektor = [0, 0]
    sekme = 0
    top_hareketli_mi = False
    top_donus_acisi = 0

def giris_menusu():
    screen.blit(arkaplan_resmi, (0, 0))
    baslik = baslik_font.render("Futbol Oyunu", True, WHITE)
    giris_text = font.render("ENTER - Başlat", True, GREEN)
    cikis_text = font.render("ESC - Çıkış", True, RED)
    screen.blit(baslik, (WIDTH // 2 - baslik.get_width() // 2, 160))
    screen.blit(giris_text, (WIDTH // 2 - giris_text.get_width() // 2, 250))
    screen.blit(cikis_text, (WIDTH // 2 - cikis_text.get_width() // 2, 290))
    pygame.display.flip()

# Ana Oyun Döngüsü
while True:
    if menu:
        giris_menusu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            menu = False
            start_time = time.time()
            skor = 0
            total_atislar = 0
            gecen_sure = 0
            reset_top()
            hoop = random_hoop()
        elif keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        continue
