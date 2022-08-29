# -*- coding: utf-8 -*-
"""
Main module for defining toy robot

"""


from controller import Controller
from table import Table
from terrain import Terrain
 

class Robot:
    """
    The main robot class which does most of the action here
    """
    valid_directions = ["NORTH", "EAST", "SOUTH", "WEST"]

    def __init__(self, terrain: Terrain = None):
 
        self.terrain = terrain
        self.ready = False
        self.controller = Controller()

    def set_terrain(self, terrain: Terrain):
        """
        sets terrain for your robot
        """
        self.terrain = terrain

    def place(self, x_coord: int, y_coord: int, direction: str):
        """
        places robot in a given setting
        """
        if self.terrain is None:
            raise ValueError("""Unless robot knows the terrain,
            placement is not possible. Please specify terrain by running
            <robot>.set_terrain(<terrain>)""")

        if(self.terrain.coords_within_boundary(x_coord, y_coord) and
           direction in self.valid_directions):
            self.ready = True
            self.controller.update(x_coord,
                                          y_coord,
                                          direction,
                                          self.terrain)
        #else:
            #logger.error("Not a valid position or direction on table.")

    def position(self):
        """
        reports position of robot
        """
        return (self.controller.x,
                self.controller.y, self.controller.direction)

    def report(self):
        """
        generic report function
        """
        return str(self)

    def __str__(self) -> str:
        status = str(self.controller)
        return status
