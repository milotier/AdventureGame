from Tkinter import *
from Player import *

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
                     "directions": {EAST: None, SOUTH: None}},
                    {"title": "field (0,1)",
                     'items': [],
                     "description": "this is a test field.",
                     "directions": {NORTH: None, EAST: None, SOUTH: None}},
                    {"title": "field (0,2)",
                     'items': [],
                     "description": "this is a test field.",
                     "directions": {NORTH: None, EAST: None}}], 
                    [{"title": "field (1,0)",
                     'items': [],
                     "description": "this is a test field.",
                     "directions": {EAST: None, SOUTH: None, WEST: None}},
                    {"title": "field (1,1)",
                     'items': ['dynamite'],
                     "description": "this is a test field with an item.",
                     "directions": {NORTH: None, EAST: None, SOUTH: None, WEST: None}},
                    {"title": "field (1,2)",
                     'items': [],
                     "description": "this is a test field.",
                     "directions": {NORTH: None, EAST: None, WEST: None}}],
                    [{"title": "field (2,0)",
                     'items': [],
                     "description": "this is a test field.",
                     "directions": {SOUTH: None, WEST: None}},
                    {"title": "field (2,1)",
                     'items': [],
                     "description": "this is a test field with an obstacle.",
                     "directions": {NORTH: None, EAST: {'name': 'a stone wall', 'weakness': 'dynamite'}, SOUTH: None, WEST: None}},
                    {"title": "field (2,2)",
                     'items': ['a sword'],
                     "description": "this is a test field with an item.",
                     "directions": {NORTH: None, WEST: None}}],
                    [{'title': 'a secret room (3,0)',
                     'items': ['money'],
                     'description': 'this is a secret room.',
                     'directions': {SOUTH: None}},
                    {'title': 'field (3,1)',
                     'items': [],
                     'description': 'this is a test field with multiple obstacles',
                     'directions': {NORTH: {'name': 'a sleeping dragon', 'weakness': 'a sword'}, EAST: {'name': 'a city guard', 'weakness': 'money'}, WEST: None}}], 
                    [{},
                    {'title': 'the western city gate (4,1)',
                    'items': [],
                    'description': 'this is the western gate of the biggest city in the realm.',
                    'directions': {WEST: None}}]
                    ]

    def giveSummary(self, direction):
        if direction == NORTH:
            return self.worldDef[self.xCoordinate][self.yCoordinate-1]['title']

        elif direction == EAST:
            return self.worldDef[self.xCoordinate+1][self.yCoordinate]['title']

        elif direction == SOUTH:
            return self.worldDef[self.xCoordinate][self.yCoordinate+1]['title']

        elif direction == WEST:
            return self.worldDef[self.xCoordinate-1][self.yCoordinate]['title']

            
    def giveRoom(self, direction):
        if direction == NORTH:
            self.yCoordinate -= 1

        elif direction == EAST:
            self.xCoordinate += 1

        elif direction == SOUTH:
            self.yCoordinate += 1

        elif direction == WEST:
            self.xCoordinate -= 1

    def getItemFromIndex(self, index):
        item = self.worldDef[self.xCoordinate][self.yCoordinate]['items'][index[0]]
        return item

    def removeItemFromCurrentLocation(self, item):
        removeItem = self.worldDef[self.xCoordinate][self.yCoordinate]['items'][item[0]]
        self.worldDef[self.xCoordinate][self.yCoordinate]['items'].remove(removeItem)

    def addItemToCurrentLocation(self, item):
        addItem = item
        self.worldDef[self.xCoordinate][self.yCoordinate]['items'].append(addItem)

    def checkObstacleSide(self, screenDef, obstacle):
        if obstacle == False:
            if NORTH in screenDef['directions'] and screenDef['directions'][NORTH] != None:
                obstacleSide = NORTH

            if EAST in screenDef['directions'] and screenDef['directions'][EAST] != None:
                obstacleSide = EAST

            if SOUTH in screenDef['directions'] and screenDef['directions'][SOUTH] != None:
                obstacleSide = SOUTH

            if WEST in screenDef['directions'] and screenDef['directions'][WEST] != None:
                obstacleSide = WEST

        else:
            currentSide = NORTH 
            obstacleSide = 0 
            for direction in screenDef['directions']:
                if screenDef['directions'][direction] == obstacle:
                    obstacleSide = currentSide
                currentSide += 1
        
        return obstacleSide

    def getObstacleFromCurrentLocation(self, screenDef):
        for direction in screenDef['directions']:
            if screenDef['directions'][direction] != None:
                obstacle = screenDef['directions'].get(direction)
        return obstacle

    def getObstacleFromString(self, obstacleString, screenDef):
        for direction in screenDef['directions']:
            if 'name' in screenDef['directions'][direction]:
                if obstacleString == screenDef['directions'][direction]['name']:
                    obstacle = screenDef['directions'].get(direction)
                    break
        return obstacle

    def checkHowManyObstacles(self):
        self.obstacleNum = 0
        for direction in self.worldDef[self.xCoordinate][self.yCoordinate]['directions']:
            self.directionValue = self.worldDef[self.xCoordinate][self.yCoordinate]['directions'].get(direction)
            if self.directionValue != None:
                self.obstacleNum += 1
        return self.obstacleNum

    def checkForRightItem(self, item, obstacle):
        if item == obstacle['weakness']:
            rightCombination = True
        else:
            rightCombination = False
        
        return rightCombination

    def removeObstacleFromCurrentLocation(self, obstacle):
        if obstacle == NORTH:
            self.worldDef[self.xCoordinate][self.yCoordinate]['directions'][NORTH] = None

        elif obstacle == EAST:
            self.worldDef[self.xCoordinate][self.yCoordinate]['directions'][EAST] = None

        elif obstacle == SOUTH:
            self.worldDef[self.xCoordinate][self.yCoordinate]['directions'][SOUTH] = None

        elif obstacle == WEST:
            self.worldDef[self.xCoordinate][self.yCoordinate]['directions'][WEST] = None
        
        

    
    
