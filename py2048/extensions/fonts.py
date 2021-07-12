from pygame.sysfont import SysFont


class LazyFont:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

        self._proxy = None

    def render(self, *args, **kwargs):
        if self._proxy is None:
            self._proxy = SysFont(*self.args, **self.kwargs)
        return self._proxy.render(*args, **kwargs)
