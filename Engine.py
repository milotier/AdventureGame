from Tkinter import *
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
        self.gameScreen.makeScreen(self.world.worldDef[self.world.xCoordinate][self.world.yCoordinate])
        self.gameScreen.updateScreen(self.world.worldDef[self.world.xCoordinate][self.world.yCoordinate], self.player.inventory)
        self.window.mainloop()

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

        self.nextRoom()

    def pickUpItem(self, item):
        selectedItem = self.world.getItemFromIndex(item)
        self.world.removeItemFromCurrentLocation(item)
        self.player.addItemToInventory(selectedItem)
        self.nextRoom()    

    def dropItem(self, item):
        selectedItem = self.player.getItemFromIndex(item)
        self.world.addItemToCurrentLocation(selectedItem)
        self.player.removeItemFromInventory(selectedItem)
        self.nextRoom()

    def useItem(self, item):
        selectedItem = self.player.getItemFromIndex(item)
        obstacleNum = self.world.checkHowManyObstacles()
        if obstacleNum == 0:
            self.gameScreen.cantUseItem('no obstacle')

        if obstacleNum == 1:
            obstacle = self.world.getObstacleFromCurrentLocation(self.world.worldDef[self.world.xCoordinate][self.world.yCoordinate])
            obstacleSide = self.world.checkObstacleSide(self.world.worldDef[self.world.xCoordinate][self.world.yCoordinate], False)
            rightItem = self.world.checkForRightItem(selectedItem, obstacle) 
            if rightItem:
                self.player.removeItemFromInventory(selectedItem)
                self.world.removeObstacleFromCurrentLocation(obstacleSide)
                self.nextRoom()
            else:
                self.gameScreen.cantUseItem('wrong obstacle')
        elif obstacleNum > 1:
            self.gameScreen.askWhichObstacle(self.world.worldDef[self.world.xCoordinate][self.world.yCoordinate], item)

    def removeObstacle(self, obstacleName, item):
        selectedItem = self.player.getItemFromIndex(item)
        chosenObstacle = self.world.getObstacleFromString(obstacleName, self.world.worldDef[self.world.xCoordinate][self.world.yCoordinate])
        rightObstacleChosen = self.world.checkForRightItem(selectedItem, chosenObstacle)
        if rightObstacleChosen:
            obstacleSide = self.world.checkObstacleSide(self.world.worldDef[self.world.xCoordinate][self.world.yCoordinate], chosenObstacle)
            self.gameScreen.destroyPopupmessage()
            self.player.removeItemFromInventory(selectedItem)
            self.world.removeObstacleFromCurrentLocation(obstacleSide)
            self.nextRoom()
        else:
            self.gameScreen.cantUseItem('wrong obstacle')

    def giveSummary(self, direction):
        return self.world.giveSummary(direction)
        
game = Engine()
game.start()