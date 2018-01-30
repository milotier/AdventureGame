from Tkinter import *

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
                     "description": "this is a test field.",
                     'items': [],
                     "directions": (False, True, True, False)},
                    {"title": "field (0,1)",
                     'items': [],
                     "description": "this is a test field.",
                     "directions": (True, True, True, False)},
                    {"title": "field (0,2)",
                     'items': [],
                     "description": "this is a test field.",
                     "directions": (True, True, False, False)}], 
                    [{"title": "field (1,0)",
                     'items': [],
                     "description": "this is a test field.",
                     "directions": (False, True, True, True)},
                    {"title": "field (1,1)",
                     'items': ['test item'],
                     "description": "this is a test field with an item.",
                     "directions": (True, True, True, True)},
                    {"title": "field (1,2)",
                     'items': [],
                     "description": "this is a test field.",
                     "directions": (True, True, False, True)}],
                    [{"title": "field (2,0)",
                     'items': [],
                     "description": "this is a test field.",
                     "directions": (False, False, True, True)},
                    {"title": "field (2,1)",
                     'items': [],
                     "description": "this is a test field.",
                     "directions": (True, False, True, True)},
                    {"title": "field (2,2)",
                     'items': [],
                     "description": "this is a test field.",
                     "directions": (True, False, False, True)}],
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

    def removeItemFromCurrentLocation(self, item):
        self.worldDef[self.xCoordinate][self.yCoordinate]['items'].remove(item)
        

    
    
