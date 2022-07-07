from enum import Enum
from math import floor
from typing import Tuple

from PIL import Image, ImageDraw

class Sierpinski:
    class RECURSIONMODE(Enum):
        FILLED = 1
        REMOVED = 2
        BOTH = 3

    def __init__(self, size:Tuple[int, int], iterations:int, tiles:Tuple[int, int]=(1,1), loc:Tuple[int, int]=(0,0), mode:str="F"):
        self._size  = size
        self._loc   = loc
        self._tiles = tiles
        self._mode  = mode
        self._im    = self._generate(iterations=iterations)

    @property
    def Width(self):
        return self._size[0]
    @property
    def Height(self):
        return self._size[1]

    @property
    def XTiles(self):
        return self._tiles[0]
    @property
    def YTiles(self):
        return self._tiles[1]

        
    def _generate(self, iterations:int):
        im = Image.new(mode=self._mode, size=self._size, color=(0, 0, 0))
        tile_width  = floor(self.Width  / self.XTiles)
        tile_height = floor(self.Height / self.YTiles)

        return im

