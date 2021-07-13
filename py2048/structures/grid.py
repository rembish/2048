from random import randint, choice

import pygame

from py2048.constants import COLOR_GRID_BACKGROUND, COLOR_GRID_BORDER, TILES_PER_ROW, TILES_PER_COLUMN, TILE_WIDTH, \
    BORDER_WIDTH, SCREEN_HEIGHT, TILE_HEIGHT, SCREEN_WIDTH
from py2048.structures.tile import Tile


class Grid:
    def __init__(self):
        self._surface = pygame.display.get_surface()
        self.sprites = pygame.sprite.Group()

        self.tiles = []
        for y in range(TILES_PER_COLUMN):
            self.tiles.append([None] * TILES_PER_ROW)

        self.draw()

    def draw(self):
        self._surface.fill(COLOR_GRID_BACKGROUND)

        for x in range(TILES_PER_ROW + 1):
            pygame.draw.rect(
                self._surface, COLOR_GRID_BORDER,
                pygame.Rect(x * (TILE_WIDTH + BORDER_WIDTH), 0, BORDER_WIDTH, SCREEN_HEIGHT), 0
            )
        for y in range(TILES_PER_COLUMN + 1):
            pygame.draw.rect(
                self._surface, COLOR_GRID_BORDER,
                pygame.Rect(0, y * (TILE_HEIGHT + BORDER_WIDTH), SCREEN_WIDTH, BORDER_WIDTH), 0
            )

    def __str__(self):
        full = ""
        for y in range(TILES_PER_COLUMN):
            row = ""
            for x in range(TILES_PER_ROW):
                current = self.tiles[y][x]
                if current is None:
                    row += "."
                else:
                    row += str(current.value)
            full += row + "\n"
        return full

    def get_empty(self):
        empty = []
        for y in range(TILES_PER_COLUMN):
            for x in range(TILES_PER_ROW):
                if self.tiles[y][x] is None:
                    empty.append((x, y))
        return empty

    def place_tile(self):
        empty = self.get_empty()
        if not empty:
            return None

        (x, y) = choice(empty)
        tile = self.tiles[y][x] = Tile.create_on(x, y)
        self.sprites.add(tile)
        return tile

    def move_left(self):
        changed = False
        for y in range(TILES_PER_COLUMN):
            for x in range(TILES_PER_ROW):
                current = self.tiles[y][x]
                if current is None:
                    continue

                for x2 in range(x - 1, -1, -1):
                    ox, oy = current.x, current.y
                    other = self.tiles[y][x2]
                    if other is None:
                        self.tiles[y][x2] = current.move(x2, y)
                        self.tiles[oy][ox] = None
                        changed = True
                    elif current == other:
                        self.sprites.remove(current)
                        other.inc()
                        self.tiles[oy][ox] = None
                        changed = True
                        break
        return changed

    def move_right(self):
        changed = False
        for y in range(TILES_PER_COLUMN):
            for x in range(TILES_PER_ROW - 1, -1, -1):
                current = self.tiles[y][x]
                if current is None:
                    continue

                for x2 in range(x + 1, TILES_PER_ROW):
                    ox, oy = current.x, current.y
                    other = self.tiles[y][x2]
                    if other is None:
                        self.tiles[y][x2] = current.move(x2, y)
                        self.tiles[oy][ox] = None
                        changed = True
                    elif current == other:
                        self.sprites.remove(current)
                        other.inc()
                        self.tiles[oy][ox] = None
                        changed = True
                        break
        return changed

    def move_up(self):
        changed = False
        for y in range(TILES_PER_COLUMN):
            for x in range(TILES_PER_ROW):
                current = self.tiles[y][x]
                if current is None:
                    continue

                for y2 in range(y - 1, -1, -1):
                    ox, oy = current.x, current.y
                    other = self.tiles[y2][x]
                    if other is None:
                        self.tiles[y2][x] = current.move(x, y2)
                        self.tiles[oy][ox] = None
                        changed = True
                    elif current == other:
                        self.sprites.remove(current)
                        other.inc()
                        self.tiles[oy][ox] = None
                        changed = True
                        break
        return changed

    def move_down(self):
        changed = False
        for y in range(TILES_PER_COLUMN - 1, -1, -1):
            for x in range(TILES_PER_ROW):
                current = self.tiles[y][x]
                if current is None:
                    continue

                for y2 in range(y + 1, TILES_PER_COLUMN):
                    ox, oy = current.x, current.y
                    other = self.tiles[y2][x]
                    if other is None:
                        self.tiles[y2][x] = current.move(x, y2)
                        self.tiles[oy][ox] = None
                        changed = True
                    elif current == other:
                        self.sprites.remove(current)
                        other.inc()
                        self.tiles[oy][ox] = None
                        changed = True
                        break
        return changed
