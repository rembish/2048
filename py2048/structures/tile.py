import pygame

from py2048.constants import TILE_VALUE_FUNC, COLOR_TILE, BORDER_WIDTH, TILE_WIDTH, TILE_HEIGHT, TILE_FONT, \
    COLOR_TILE_FONT, COLOR_TILE_FONT_2


class Tile(pygame.sprite.Sprite):
    hash = 0

    def __init__(self, x, y, *, value=2):
        super().__init__()
        self.x = x
        self.y = y
        self.value = value

        Tile.hash += 1
        self._hash = Tile.hash

        self.surface = pygame.Surface((TILE_WIDTH, TILE_HEIGHT))

        self.draw()

    def __repr__(self):
        return f"<{self.__class__.__name__}#{self.x}{self.y}: {self.value}>"

    def __eq__(self, other):
        return self.value == other.value

    def __hash__(self):
        return self._hash

    @property
    def rectangle(self):
        return self.surface.get_rect(center=self.get_position())

    def get_position(self):
        return (
            BORDER_WIDTH + TILE_WIDTH // 2 + 1 + self.x * (BORDER_WIDTH + TILE_WIDTH),
            BORDER_WIDTH + TILE_HEIGHT // 2 + 1 + self.y * (BORDER_WIDTH + TILE_HEIGHT),
        )

    def draw(self):
        self.surface.fill(COLOR_TILE[self.value])
        text = TILE_FONT.render(str(self.value), True, COLOR_TILE_FONT_2 if self.value > 4 else COLOR_TILE_FONT)
        text_rectangle = text.get_rect(center=(TILE_WIDTH // 2 + 1, TILE_HEIGHT // 2 + 1))
        self.surface.blit(text, text_rectangle)

    def move(self, x, y):
        self.x, self.y = x, y
        return self

    def inc(self):
        self.value *= 2
        self.draw()

    @classmethod
    def create_on(cls, x, y, *, value=None):
        if value is None:
            value = TILE_VALUE_FUNC()

        return cls(x, y, value=value)
