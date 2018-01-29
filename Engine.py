from tkinter import *
from GameScreen import *
from World import *
from Player import *

class Engine:
    def __init__(self):
        self.window = Tk()
        self.window.title('Adventure Game')
        self.window.geometry('600x500')
        self.gameScreen = GameScreen(self)
        self.world = World(self)
        self.player = Player(self)

    def start(self):
        self.gameScreen.makeScreen(self.world.worldDef[self.world.xCoordinate][self.world.yCoordinate], self.player.inventory)

    def nextRoom(self):
        self.gameScreen.updateScreen(self.world.worldDef[self.world.xCoordinate][self.world.yCoordinate], self.player.inventory)

    def askNextRoom(self, direction):
        if direction == NORTH:
            self.world.giveRoom(NORTH)

        if direction == EAST:
            self.world.giveRoom(EAST)

        if direction == SOUTH:
            self.world.giveRoom(SOUTH)

        if direction == WEST:
            self.world.giveRoom(WEST)

    def pickUpItem(self, item):
        self.world.removeItemFromCurrentLocation(item)
        self.player.addItemToInventory(item)
        self.gameScreen.updateScreen(self.world.worldDef[self.world.xCoordinate][self.world.yCoordinate], self.player.inventory)       
        
game = Engine()
game.start()
