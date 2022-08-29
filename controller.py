# -*- coding: utf-8 -*-
"""
 Coordinate and movement class
"""

from math import cos, radians, sin
from table import Table
from terrain import Terrain

import turtle

DICT_DIRECTIONS = {"NORTH": 90, "SOUTH": 270, "EAST": 0, "WEST": 180}
DICT_DEGREES = {90: "NORTH", 270: "SOUTH", 0: "EAST", 180: "WEST"}

class Controller:
    """
    Controller class to handle the robot movement
    """
   

    def __init__(self, x: int = None,
                 y: int = None,
                 direction: str = None,
                 terrain: Terrain = None):
        self.x = x
        self.y = y
        self.direction = direction
        self.degree = DICT_DIRECTIONS.get(direction, None)
        self.terrain = terrain
        
        turtle.color("black", "red")
        #turtle.begin_fill()
        #turtle.shape("square")
        turtle.shapesize(5,5,1)
        #turtle.end_fill()

    def set_terrain(self, terrain: Terrain):
        """
             Sets the terrain for controller
        """
        self.terrain = terrain

    def update(self, x: int, y: int,
               direction: str = None,
               terrain: Terrain = None):
        """
        updates the current position of the robot 
        """

        self.terrain = terrain if terrain is not None else self.terrain
        if direction in DICT_DIRECTIONS.keys():
            self.x = x
            self.y = y
            self.direction = direction if direction is not None \
                else self.direction
            self.degree = DICT_DIRECTIONS.get(direction, None)
        turtle.setx(self.x)
        turtle.sety(self.y)
        turtle.setheading(self.degree)


    def move(self):
        """
        Move one step at a time
        """
        try:
            new_x = self.x + int(cos(radians(self.degree)))
            new_y = self.y + int(sin(radians(self.degree)))
            if self.terrain.coords_within_boundary(new_x, new_y):
                self.update(new_x, new_y, self.direction)
                turtle.forward(1)
                turtle.position(new_x, new_y)
            return (self.x, self.y)
        except TypeError as te:
            pass
        
        

    def left(self):
        """
        Face left
        """
        try:
            self.degree += 90
            self.degree = self.degree % 360
            self.direction = DICT_DEGREES.get(self.degree)
            turtle.left(90)
        except TypeError as te:
            pass

    def right(self):
        """
        Face right
        """
        try:
            self.degree -= 90
            self.degree = self.degree % 360
            self.direction = DICT_DEGREES.get(self.degree)
            turtle.right(90)
        except TypeError as te:
            pass
            

    def __str__(self) -> str:
        """
        for reporting
        """
        turtle.goto(self.x,self.y)
        return "Coordinate(x,y): {x}, {y}. Position {direction}".format(
            x=self.x,
            y=self.y, direction=self.direction)
