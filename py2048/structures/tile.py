import pygame

from py2048.constants import TILE_VALUE_FUNC, COLOR_TILE, BORDER_WIDTH, TILE_WIDTH, TILE_HEIGHT, TILE_FONT, \
    COLOR_TILE_FONT


class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, *, value=2):
        super().__init__()
        self.x = x
        self.y = y
        self.value = value

        self.surface = pygame.Surface((TILE_WIDTH, TILE_HEIGHT))
        self.surface.fill(COLOR_TILE[self.value])
        text = TILE_FONT.render(str(value), True, COLOR_TILE_FONT)
        text_rectangle = text.get_rect(center=(TILE_WIDTH // 2 + 1, TILE_HEIGHT // 2 + 1))
        self.surface.blit(text, text_rectangle)
        self.rectangle = self.surface.get_rect(center=self.get_position())

    def __repr__(self):
        return f"<{self.__class__.__name__}#{self.x}{self.y}: {self.value}>"

    def get_position(self):
        return (
            BORDER_WIDTH + TILE_WIDTH // 2 + 1 + self.x * (BORDER_WIDTH + TILE_WIDTH),
            BORDER_WIDTH + TILE_HEIGHT // 2 + 1 + self.y * (BORDER_WIDTH + TILE_HEIGHT),
        )

    @classmethod
    def create_on(cls, x, y, *, value=None):
        if value is None:
            value = TILE_VALUE_FUNC()

        return cls(x, y, value=value)
