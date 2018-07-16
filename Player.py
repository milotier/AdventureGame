from Tkinter import *

class Player:
    def __init__(self, engine):
        self.engine = engine
        self.inventory = []
        self.maximalHP = 50
        self.currentHP = 50

    def getItemFromIndex(self, index):
        item = self.inventory[index[0]]
        return item

    def addItemToInventory(self, item):
        self.inventory.append(item)

    def removeItemFromInventory(self, item):
        self.inventory.remove(item)
