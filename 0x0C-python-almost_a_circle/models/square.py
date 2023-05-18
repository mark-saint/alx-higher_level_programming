#!/usr/bin/python3
"""
this is a square file
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    this is a square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        super(Square, self).__init__(size, size, x, y, id)

    def __str__(self):
        """
        str representation
        """
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__,
                                             self.id, self.x,
                                             self.y, self.width)

    @property
    def size(self):
        """
        return size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        seter
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
