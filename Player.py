from Tkinter import *

class Player:
    def __init__(self, engine):
        self.engine = engine
        self.inventory = []

    def addItemToInventory(self, item):
        self.inventory.append(item)
