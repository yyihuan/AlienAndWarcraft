import pygame
import sys

def check_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:  print(event.key)

pygame.init()
while 1:
    check_event()
