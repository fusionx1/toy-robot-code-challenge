# -*- coding: utf-8 -*-
"""
Main module for Table class

"""

class Table():
    """
    Table on which robot will be placed
    """

    def __init__(self, length, width):
        if (length < 1 or width < 1):
            raise ValueError("Table length and width should be more than 0")
       
        self.length = length
        self.width = width

    def coords_within_boundary(self, x_pos: int, y_pos: int) -> bool:
        """
        Given x and y coordinates return if the location of the robot is still with the boundary
        """
       
        return (0 <= x_pos <= self.width) and (0 <= y_pos <= self.length)

    def __str__(self):
        return "Width: {width}, Length: {length}".format(width=self.width,
                                                         length=self.length)
