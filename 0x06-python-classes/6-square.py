#!/usr/bin/python3
"""
Cool stuff
"""


class Square:
    """
    Square class
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Args:
            size: sth
        """
        self.__position = position
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Area here we go
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Returns size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        size setter:
        Args:
            value: new value
        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("size must be as integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
        Returns:
            a print
        """
        if self.__size == 0:
            return
        for _ in range(self.__size):
            k = "_" * self.__position[0] + "#" * self.__size
            print(k)
    
    @property
    def position(self):
        """
        Return:
            position
        """
        return self.__position

    @position.setter
    def position(self, position):
        """
        Args:
            position: th
        Returns:
            None
        """
        self.__position = position
