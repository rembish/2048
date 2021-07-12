from random import seed

import pygame

from py2048.constants import TILE_AFTER_START
from py2048.structures.grid import Grid


class Application:
    def __init__(self, *, width=640, height=480):
        self.width, self.height = width, height
        self._running = False
        self._surface = None
        self._grid = None
        self._sprites = pygame.sprite.Group()

    def initialize(self):
        pygame.init()
        pygame.font.init()
        seed()

        self._surface = pygame.display.set_mode((self.width, self.height), pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption("2048")
        self._running = True

        self._grid = Grid()
        for _ in range(TILE_AFTER_START):
            tile = self._grid.place_tile()
            self._sprites.add(tile)

    def cleanup(self):
        pygame.font.quit()
        pygame.quit()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        for entity in self._sprites:
            self._surface.blit(entity.surface, entity.rectangle)

        pygame.display.update()

    def run(self):
        self.initialize()

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)

            self.on_loop()
            self.on_render()

        self.cleanup()
