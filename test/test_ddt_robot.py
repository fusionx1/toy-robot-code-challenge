# -*- coding: utf-8 -*-
"""
DDT testing Robot class

"""
import unittest

from ddt import data, ddt, unpack

from robot import Robot
from table import Table
from terrain import Terrain

@ddt
class RobotTest(unittest.TestCase):
    """
    Tests for Robot Simulator
    """

    def setUp(self):
        self.terrain = Table(50, 50)
        self.robot = Robot(self.terrain)

    def test_report_robot_if_created_properly(self):
        self.assertFalse(self.robot.ready)
        self.assertEqual(self.robot.position(), (None, None, None))
        self.assertEqual(self.robot.terrain, self.terrain)

    def test_if_robot_is_not_on_table(self):
        robot_in_air = Robot()
        self.assertFalse(robot_in_air.ready)
        self.robot.controller.move()
        self.robot.controller.left()
        self.robot.controller.right()
        self.assertEqual(self.robot.position(), (None, None, None))

    @data((0, 0, "NORTH"), (30, 40, "EAST"), (10, 20, "NORTH"))
    @unpack
    def test_report_placing_robot_correctly(self, x_coord, y_coord, direction):
        self.robot.place(x_coord, y_coord, direction)
        self.assertEqual(self.robot.ready, True)
        self.assertEqual(self.robot.position(), (x_coord, y_coord, direction))
       

    def test_report_discard_until_placing_robot(self):
        newbot = Robot(self.terrain)
        newbot.controller.move()
        newbot.controller.move()
        newbot.controller.left()
        self.assertEqual(self.robot.position(), (None, None, None))

    @data((0, 0, "NORTH"), (12, 30, "EAST"), (20, 40, "NORTH"))
    @unpack
    def test_when_robot_trying_to_go_beyond_boundary(self, x_coord,
                                               y_coord, direction):
        self.robot.place(x_coord, y_coord, direction)
        self.assertEqual(self.robot.ready, True)
        
        for x in range(0, 10):
            self.robot.controller.move()
        (x, y, _d) = self.robot.position()
        self.assertTrue(self.terrain.coords_within_boundary(x,y))


    @data((0, 0, "NORTH"), (35, 15, "EAST"), (20, 40, "WEST"), (25, 30, "SOUTH"))
    @unpack
    def test_robot_position(self, x, y, d):
        self.robot.place(x, y, d)
        exp = "Coordinate(x,y): {x}, {y}. Position {direction}".format(x=x,
                                                                       y=y,
                                                                       direction=d)
        self.assertEqual(self.robot.report(), exp)
