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
