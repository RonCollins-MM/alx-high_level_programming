#!/usr/bin/python3
"""Square Class Module"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square Class implementation.

    Inherits from Rectangle class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns a string representation of Square instance"""
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'

    @property
    def size(self):
        """Getter for size"""
        return self.height

    @size.setter
    def size(self, size):
        """Setter for size"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Updates the attributes of Square instance"""
        count = 0
        if args:
            for i in args:
                if count == 0:
                    self.id = i
                    count += 1
                    continue
                if count == 1:
                    self.size = i
                    count += 1
                    continue
                if count == 2:
                    self.x = i
                    count += 1
                    continue
                if count == 3:
                    self.y = i
                    count += 1
                    continue
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """Generates a dictionary object of Square instance"""
        return {'id': self.id, 'x': self.x,
                    'size': self.height, 'y': self.y}
