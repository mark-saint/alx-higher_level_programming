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

    def update(self, *args, **kwargs):
        """updates the rec"""
        len_args = len(args)

        if len_args != 0:
            if len_args < 2:
                self.id = args[0]
            elif len_args < 3:
                self.id = args[0]
                self.size = args[1]
            elif len_args < 4:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
            elif len_args < 5:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]

        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.width = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
