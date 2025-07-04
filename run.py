import pygame
from pygame.locals import *
from contansts import *
from pacman import Pacman
from nodes import NodeGroup

class GameController(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((36*16,28*16))
        self.background = None
        self.clock = pygame.time.Clock()
        #self.pacman = Pacman()
        
    def setBackground(self):
        self.background = pygame.surface.Surface((36*16,28*16)).convert()
        self.background.fill(BLACK)
        
    def startGame(self):
        self.setBackground()
        self.nodes = NodeGroup()
        self.nodes.setupTestNodes()
        self.pacman = Pacman(self.nodes.nodeList[0])
    
    def update(self):
        dt = self.clock.tick(30) / 1000.0
        self.pacman.update(dt)
        self.checkEvents()
        self.render()
        
    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
    
    def render(self):
        self.screen.blit(self.background,(0,0))
        self.nodes.render(self.screen)
        self.pacman.render(self.screen)
        pygame.display.update()
        
if __name__ == "__main__":
        game = GameController()
        game.startGame()
        while True:
            game.update()