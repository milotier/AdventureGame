from Tkinter import *

class InteractionController:

    def __init__(self, engine, world, player, navigationController):
        self.engine = engine
        self.world = world
        self.player = player
        self.navigationController = navigationController

    def setGameScreen(self, gameScreen):
        self.gameScreen = gameScreen

    def pickUpItem(self, item):
        selectedItem = self.world.getItemFromIndex(item)
        self.world.removeItemFromCurrentLocation(item)
        self.player.addItemToInventory(selectedItem)
        self.navigationController.nextRoom()    

    def dropItem(self, item):
        selectedItem = self.player.getItemFromIndex(item)
        self.world.addItemToCurrentLocation(selectedItem)
        self.player.removeItemFromInventory(selectedItem)
        self.navigationController.nextRoom()

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
                self.navigationController.nextRoom()
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
            self.navigationController.nextRoom()
        else:
            self.gameScreen.cantUseItem('wrong obstacle')
