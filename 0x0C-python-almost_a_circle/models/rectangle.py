#!/usr/bin/python3
"""Rectangle Class Module"""

from models.base import Base

class Rectangle(Base):
    """
    Rectangle Class implementation. Inherits from Base Class.

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor.
        All Rectangle objects must be instantiated with a specified width and
        height.

        Args:
            width (int) - Width of Rectangle object
            height (int) - Height of Rectangle object
            x (int, optional) - x coordinate of Rectangle object
            y (int, optional) - y coordinate of Rectangle object
            id (int, optional) - id of Rectangle object

        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Setter for width"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter for height"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Setter for x"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, y):
        """Setter for y"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Calculates area of Rectangle instance.

        Returns:
            Area
        """
        return self.__width * self.__height

    def display(self):
        """Prints instance of Rectangle class with ``#`` symbol """
        if self.__y > 0:
            print("\n" * self.__y, end="")
        for i in range(self.__height):
            if self.__x > 0:
                print(" " * self.__x, end="")
            for j in range(self.__width):
                print("#", end="")
            if i < self.__height:
                print()

    def __str__(self):
        """Returns a string representation of Rectangle class"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} -
        {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """Updates attributes of an instance of Rectangle class"""
        count = 0
        if args:
            for i in args:
                if count == 0:
                    self.id = i
                    count += 1
                    continue
                if count == 1:
                    self.width = i
                    count += 1
                    continue
                if count == 2:
                    self.height = i
                    count += 1
                    continue
                if count == 3:
                    self.x = i
                    count += 1
                    continue
                if count == 4:
                    self.y = i
                    count += 1
                    continue
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """Generates a dictionary object of a Rectangle instance"""
        return {'x': self.x, 'y': self.y, 'id': self.id,
                    'height': self.height, 'width': self.width}
