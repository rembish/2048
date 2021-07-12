from random import seed

import pygame

from py2048.structures.grid import Grid


class Application:
    starting_tiles = 2

    def __init__(self, *, width=640, height=480):
        self.width, self.height = width, height
        self._running = False
        self._surface = None
        self._grid = None

    def initialize(self):
        pygame.init()
        seed()

        self._surface = pygame.display.set_mode((self.width, self.height), pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

        self._grid = Grid()
        for _ in range(self.starting_tiles):
            self._grid.place_tile()

    def cleanup(self):
        pygame.quit()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        pygame.display.update()

    def run(self):
        self.initialize()

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)

            self.on_loop()
            self.on_render()

        self.cleanup()
