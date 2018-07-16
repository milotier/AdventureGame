from Tkinter import *
from World import NORTH, EAST, SOUTH, WEST


class NavigationController:
    def __init__(self, engine, world, player):
        self.engine = engine
        self.world = world
        self.player = player

    def setGameScreen(self, gameScreen):
        self.gameScreen = gameScreen

    def askNextRoom(self, direction):
        if direction == NORTH:
            self.world.giveRoom(NORTH)

        if direction == EAST:
            self.world.giveRoom(EAST)

        if direction == SOUTH:
            self.world.giveRoom(SOUTH)

        if direction == WEST:
            self.world.giveRoom(WEST)

        self.nextRoom()

    def nextRoom(self):
        self.gameScreen.updateScreen(self.world.worldDef[self.world.xCoordinate][self.world.yCoordinate], self.player.inventory, self.player.currentHP, self.player.maximalHP)