#faça um programa em python que abra e reproduza o audio de um arquivo MP3.
'''REVISÃO'''

import pygame
pygame.init()
pygame.mixer.music.load()
pygame.mixer.music.play()
pygame.event.wait()