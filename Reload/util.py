import pygame

def blit_by_item(item, screen):
    screen.blit(item['image'], item['position'])

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('ReLOAD')