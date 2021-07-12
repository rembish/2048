class Tile:
    def __init__(self, x, y, *, value=2):
        self.x = x
        self.y = y
        self.value = value

    def __repr__(self):
        return f"<{self.__class__.__name__}#{self.x}{self.y}: {self.value}>"
