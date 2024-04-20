import pygame, sys
from settings import *
from level import Level 

class Game:
    def __init__(self): ## init method
        pygame.init() ### iniciamos pygame
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) ### creamos display surface
        pygame.display.set_caption('Bisi Mount') ### titulo de la ventana de juego
        self.clock = pygame.time.Clock() ### creamos un reloj
        self.level = Level()
    
    def run(self): ## run method
        while True: ### game loop
            for event in pygame.event.get(): #### comprueba si hemos cerrado el juego
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    sys.exit()
            
            dt = self.clock.tick() / 1000 #### delta time
            self.level.run(dt)
            pygame.display.update() #### updating the game

if __name__ == '__main__': ## comprobamos si estamos en el archivo main, luego creamos un objeto game de la clase y llamamos al metodo run
    game = Game()
    game.run()