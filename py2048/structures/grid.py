from random import randint, choice

import pygame

from py2048.constants import COLOR_GRID_BACKGROUND, COLOR_GRID_BORDER, TILES_PER_ROW, TILES_PER_COLUMN, TILE_WIDTH, \
    BORDER_WIDTH, SCREEN_HEIGHT, TILE_HEIGHT, SCREEN_WIDTH
from py2048.structures.tile import Tile


class Grid:
    def __init__(self):
        self._surface = pygame.display.get_surface()
        self._surface.fill(COLOR_GRID_BACKGROUND)

        for i in range(TILES_PER_ROW + 1):
            pygame.draw.rect(
                self._surface, COLOR_GRID_BORDER,
                pygame.Rect(i * (TILE_WIDTH + BORDER_WIDTH), 0, BORDER_WIDTH, SCREEN_HEIGHT), 0
            )
        for i in range(TILES_PER_COLUMN + 1):
            pygame.draw.rect(
                self._surface, COLOR_GRID_BORDER,
                pygame.Rect(0, i * (TILE_HEIGHT + BORDER_WIDTH), SCREEN_WIDTH, BORDER_WIDTH), 0
            )

        self.tiles = []

        for i in range(TILES_PER_ROW):
            self.tiles.append([None] * TILES_PER_COLUMN)

    def get_empty(self):
        empty = []
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[i])):
                if self.tiles[i][j] is None:
                    empty.append((i, j))
        return empty

    def place_tile(self):
        empty = self.get_empty()
        if not empty:
            return None

        (x, y) = choice(empty)
        tile = self.tiles[x][y] = Tile.create_on(x, y)
        return tile
