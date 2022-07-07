from enum import Enum
from random import randint
from typing import List, Tuple, Union

_ColorType = Union[Tuple[int, int, int], Tuple[int, int, int, int]]

class Colorbook:
    """Class to store a collection of colors, to be accessed with the "Next" function.
    The Colorbook "mode" sets the method for iterating through the list.
    """
    class MODE(Enum):
        """Enumerated type to set the mode of advancing through the Colorbook.
        """
        CONSTANT = 1
        LINEAR = 2
        BINARY_TREE  = 3
        TRINARY_TREE = 4
        RANDOM = 5

    def __init__(self, color_list:List[_ColorType], bg_color:_ColorType=(0,0,0,1), mode:MODE=MODE.LINEAR):
        self._colors = color_list
        self._bg     = bg_color
        self._mode   = mode
        self._next   = 0

    def __getitem__(self, index:int):
        idx = index % len(self._colors)
        return self._colors[idx]

    def __setitem__(self, index:int, color:_ColorType):
        if index < 0 or index > len(self._colors):
            return
        else:
            self._colors[index] = color

    def Append(self, color:_ColorType):
        """Add a color to the Colorbook.

        :param color: The color to add to the book.
        :type color: _ColorType
        """
        self._colors.append(color)

    @property
    def Background(self):
        return self._bg

    @property
    def Next(self):
        """Get next color from the Colorbook, according to the book's mode.

        :return: _description_
        :rtype: _type_
        """
        ret_val = self._colors[self._next]
        if self._mode == Colorbook.MODE.CONSTANT:
            pass
        elif self._mode == Colorbook.MODE.LINEAR:
            self._next = (self._next + 1) % len(self._colors)
        elif self._mode == Colorbook.MODE.BINARY_TREE:
            raise NotImplementedError("Binary tree mode is not yet implemented for Colorbooks.")
        elif self._mode == Colorbook.MODE.TRINARY_TREE:
            raise NotImplementedError("Trinary tree mode is not yet implemented for Colorbooks.")
        elif self._mode == Colorbook.MODE.RANDOM:
            self._next = randint(a=0, b=len(self._colors)-1)
        return ret_val
