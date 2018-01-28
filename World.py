from tkinter import *

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

class World:
    def __init__(self, engine):
        self.engine = engine
        self.xCoordinate = 0
        self.yCoordinate = 0
        self.worldDef = [
                    [{"title": "field (0,0)",
                     "description": "this is the first test field.",
                     "directions": (False, True, True, False)},
                    {"title": "field (0,1)",
                     "description": "this is the second test field.",
                     "directions": (True, True, False, False)}],
                    [{"title": "field (1,0)",
                     "description": "this is the third test field.",
                     "directions": (False, False, True, True)},
                    {"title": "field (1,1)",
                     "description": "this is the fourth test field.",
                     "directions": (True, False, False, True)}]
                    ]

    def giveRoom(self, direction):
        if direction == NORTH:
            self.yCoordinate -= 1
            self.engine.nextRoom()

        elif direction == EAST:
            self.xCoordinate += 1
            self.engine.nextRoom()

        elif direction == SOUTH:
            self.yCoordinate += 1
            self.engine.nextRoom()

        elif direction == WEST:
            self.xCoordinate -= 1
            self.engine.nextRoom()
    
