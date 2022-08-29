
# TOY ROBOT CODE CHALLENGE

Toy Robot Code Challenge

This app is based on python that simulates toy robot moving on a square table top, of demensions 5 units * 5 units；
The robot is free to roam around the surface or terrain of the table, but must be prevented from falling or go beyond the boundary set；
Any movement that would result in the robot falling from the table must be prevented. However further valid movement commands must still be allowed;

Decorators always put color in the eyes, used turtle library to present it graphically.

# These commands can be used to control the robot's movement；

* PLACE
 Put the toy robot on the table in position X,Y and facing F direction.
 Usage: PLACE X, Y, F 
 X is the x -coordinate Y is the y-coordinate F is the direction the robot is facing( NORTH, SOUTH, EAST or WEST)
 All the spaces between arguments will be ingored.
 The origin(0, 0) can be considered to be the SOUTH WEST most corner.
 It is required that the first commands to the robot is a PLACE command, after that, any sequence of commands may be issued, in any order, including another PLACE command.

All the commands before a valid PLACE command can't be executed successfully.
* MOVE
Move the toy robot one unit forward in the direction it is currently facing.
Usage: MOVE
* LEFT
Rotate the robot 90 degress to the left without changing the position of the robot.
Usage: LEFT
* RIGHT
Rotate the robot 90 degress to the right without changing the position of the robot.
Usage: RIGHT
* REPORT
Announce the X(x-coordinate on the table), Y(y-coordinate on the table) and F(facing direction) of the robot.
Usage: REPORT
Output: X: x_coordinate, Y: y_coordinate, FACING: facing direction. e.g. X: 2, Y: 2, FACING: NORTH


* Written in Python3

## Setup
- Manual
    - `virtualenv venv`
    - source `venv\bin\activate`
    - `pip install -r requirements.txt`
  


## Usage
* Run:
    `python3 main.py` 
* Help: 
    - ? for available commands
    - For particular command
      `help command`

* Exit/Quit:
    - press `q`
    - press `Ctrl + c`
 


## Test
    `python3 -m unittest tests/test_Robot.py`

