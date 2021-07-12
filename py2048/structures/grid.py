from random import randint, choice

import pygame

from py2048.structures.tile import Tile


class Grid:
    def __init__(self, *, width=4, height=4, border=10):
        self._surface = pygame.display.get_surface()
        self._border = pygame.Color(187, 173, 160)
        self._background = pygame.Color(204, 192, 180)

        surface_width, surface_height = self._surface.get_size()
        self.tile_width = (surface_width - (width + 1) * border) // width
        self.tile_height = (surface_height - (height + 1) * border) // height

        self._surface.fill(self._background)
        for i in range(width + 1):
            pygame.draw.rect(
                self._surface, self._border,
                pygame.Rect(i * (self.tile_width + border), 0, border, surface_height), 0
            )
            pygame.draw.rect(
                self._surface, self._border,
                pygame.Rect(0, i * (self.tile_height + border), surface_width, border), 0
            )

        self.tiles = []
        for i in range(width):
            self.tiles.append([None] * height)

    def get_empty(self):
        empty = []
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[i])):
                if self.tiles[i][j] is None:
                    empty.append((i, j))
        return empty

    def place_tile(self):
        value = 4 if randint(0, 100) >= 90 else 2
        empty = self.get_empty()
        if not empty:
            return None

        (x, y) = choice(empty)
        tile = self.tiles[x][y] = Tile(x, y, value=value)
        return tile
