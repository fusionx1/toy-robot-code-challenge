# -*- coding: utf-8 -*-
"""
Main module for driving the toy robot

"""

from math import degrees
import sys, cmd 

from robot import Robot
from table import Table
from terrain import Terrain
#from controller import Controller


class GameInit(cmd.Cmd):

    intro = """************************************************
    Welcome to the Toy Robot Simulator Shell
    To quit you can just type q and enter or just press Ctrl+C
    Type help or ? to list commands.\n************************************************"""
    prompt = 'Bot> '
    robot = Robot(Table(5, 5))
    

    def do_place(self, place_cmd):
        """
        Places a robot on the the defaul 5X5 table.
        Position (x,y) and facing "F"
        """
        x_coord, y_coord, direction = place_cmd.split(",")
        x_coord = int(x_coord)
        y_coord = int(y_coord)
        direction = direction.upper()
        self.robot.place(x_coord, y_coord, direction)
        #turtle.setx(x_coord)
        #turtle.sety(y_coord)
        #turtle.setheading(self.get_degree(direction))
        print("Output: {x}, {y}, {d}".format( x=x_coord, y=y_coord, d=direction))

    #def get_degree(self, direction):
    #    degrees = {"NORTH":90, "SOUTH":270, "EAST":9, "WEST":180}
    #    for k in degrees: 
    #        if k == 'NORTH':
    #            return degrees[direction]

    def do_move(self, line):
        """
        Move the robot forward by the specified distance
        """
        print(line)
        self.robot.controller.move()

    def do_left(self, _line):
        """
        Moves robot to it's left direction
        """
        self.robot.controller.left()

    def do_right(self, _line):
        """
        Moves robot to it's right direction
        """
        self.robot.controller.right()

    def do_report(self, _line):
        """
        Prints the current location of robot
        Prints nothing if robot is not "placed" yet
        """
        print(_line)
        print(self.robot.report())

    def precmd(self, line):
        line = line.lower()
        if line == "q":
            print("Exit")
            exit(0)
        return line


if __name__ == "__main__":
    GameInit().cmdloop()
