from random import randint

from pygame.color import Color

from py2048.extensions.fonts import LazyFont

SCREEN_WIDTH = 414
SCREEN_HEIGHT = 414
BORDER_WIDTH = 10

TILES_PER_ROW = 4
TILES_PER_COLUMN = 4

TILE_FONT = LazyFont("monospace", 40, bold=True)
COLOR_TILE_FONT = Color(119, 110, 101)

TILE_WIDTH = (SCREEN_WIDTH - (TILES_PER_ROW + 1) * BORDER_WIDTH) // TILES_PER_ROW
TILE_HEIGHT = (SCREEN_HEIGHT - (TILES_PER_COLUMN + 1) * BORDER_WIDTH) // TILES_PER_COLUMN

TILE_AFTER_START = 2
TILE_VALUE_FUNC = lambda: 4 if randint(0, 100) > 90 else 2

COLOR_GRID_BACKGROUND = Color(204, 192, 180)
COLOR_GRID_BORDER = Color(187, 173, 160)

COLOR_TILE = {
    2: Color(238, 228, 218),
    4: Color(237, 224, 200),
}
