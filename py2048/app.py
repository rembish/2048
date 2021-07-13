from random import seed

import pygame
from pygame.constants import K_LEFT, K_RIGHT, K_UP, K_DOWN

from py2048.constants import TILE_AFTER_START, FPS
from py2048.structures.grid import Grid


class Application:
    def __init__(self, *, width=640, height=480):
        self.width, self.height = width, height
        self._running = False
        self._surface = None
        self._grid = None
        self._clock = pygame.time.Clock()

    def initialize(self):
        pygame.init()
        pygame.font.init()
        seed()

        self._surface = pygame.display.set_mode((self.width, self.height), pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption("2048")
        self._running = True

        self._grid = Grid()
        for _ in range(TILE_AFTER_START):
            self._grid.place_tile()

    def cleanup(self):
        pygame.font.quit()
        pygame.quit()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

        pressed_keys = pygame.key.get_pressed()
        tile = 0

        if pressed_keys[K_LEFT]:
            if self._grid.move_left():
                tile = self._grid.place_tile()
        elif pressed_keys[K_RIGHT]:
            if self._grid.move_right():
                tile = self._grid.place_tile()
        elif pressed_keys[K_UP]:
            if self._grid.move_up():
                tile = self._grid.place_tile()
        elif pressed_keys[K_DOWN]:
            if self._grid.move_down():
                tile = self._grid.place_tile()

        if tile is None:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        self._grid.draw()
        for entity in self._grid.sprites:
            self._surface.blit(entity.surface, entity.rectangle)

        pygame.display.update()
        self._clock.tick(FPS)

    def run(self):
        self.initialize()

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)

            self.on_loop()
            self.on_render()

        self.cleanup()
