from curses import KEY_DOWN
import pygame
import os
import random
import time

#### EN PYGAME EL ORIGEN DE COORDENADAS ESTA EN LA ESQUINA SUPERIOR IZQUIERDA, es decir, la y esta al reves, si quieres incrementar y tienes que ir hacia abajo

# creamos la ventana
WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Marcianitos')

# load images

RED_SPACE_SHIP = pygame.image.load('assets/pixel_ship_red_small.png')
GREEN_SPACE_SHIP = pygame.image.load('assets/pixel_ship_green_small.png')
BLUE_SPACE_SHIP = pygame.image.load('assets/pixel_ship_blue_small.png')

# Player Ship
YELLOW_SPACE_SHIP = pygame.image.load('assets/pixel_ship_yellow.png')

# Lasers
RED_LASER = pygame.image.load('assets/pixel_laser_red.png')
GREEN_LASER = pygame.image.load('assets/pixel_laser_green.png')
BLUE_LASER = pygame.image.load('assets/pixel_laser_blue.png')
YELLOW_LASER = pygame.image.load('assets/pixel_laser_yellow.png')

# background

BG = pygame.image.load('assets/background-black.png')

def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock() # esta variable es la que controla el tiempo del juego

    def redraw_window():
        WIN.blit(BG, (0, 0)) # el metodo blit colocara las imagenes en la posicion, ahora mismo el fondo
        pygame.display.update() # refresca la pantalla

    while run: # este loop controla si estamos jugando
        clock.tick(FPS) # el reloj del juego hara 60 ticks por segundo, asi es como funcionara todo el juego
        redraw_window() # colocamos en pantalla

        for event in pygame.event.get(): # nos permite cerrar la ventana
            if event.type == pygame.QUIT: # si cerramos la ventana, el juego parara
                run = False

main()