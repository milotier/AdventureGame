from tkinter import *
from World import *

class GameScreen:
    def __init__(self, engine):
        self.engine = engine

    def goNorth(self):
        self.engine.askNextRoom(0)

    def goEast(self):
        self.engine.askNextRoom(1)

    def goSouth(self):
        self.engine.askNextRoom(2)

    def goWest(self):
        self.engine.askNextRoom(3)

    def makeScreen(self, screenDef):
        self.canvas = Canvas(self.engine.window, height = 500, width = 600)
        self.canvas.pack()
        Label(self.canvas, text = screenDef["title"]).place(x = 1, y = 1)
        Label(self.canvas, text = screenDef['description']).place(x = 1, y = 20)
        self.northButton = Button(self.canvas, text = 'north', command = self.goNorth)
        self.eastButton = Button(self.canvas, text = 'east', command = self.goEast)
        self.southButton = Button(self.canvas, text = 'south', command = self.goSouth)
        self.westButton = Button(self.canvas, text = 'west', command = self.goWest)
        self.northButton.place(x = 50, y = 375)
        self.eastButton.place(x = 87, y = 412)
        self.southButton.place(x = 50, y = 450)
        self.westButton.place(x = 17, y = 412)
        if not screenDef["directions"][NORTH]:
            self.northButton.config(state = DISABLED)

        if not screenDef["directions"][EAST]:
            self.eastButton.config(state = DISABLED)

        if not screenDef["directions"][SOUTH]:
            self.southButton.config(state = DISABLED)

        if not screenDef["directions"][WEST]:
            self.westButton.config(state = DISABLED)
        
