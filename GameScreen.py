from tkinter import *
from World import *

class GameScreen:
    def __init__(self, engine):
        self.engine = engine

    def goNorth(self):
        self.engine.askNextRoom(NORTH)

    def goEast(self):
        self.engine.askNextRoom(EAST)

    def goSouth(self):
        self.engine.askNextRoom(SOUTH)

    def goWest(self):
        self.engine.askNextRoom(WEST)

    def onPickUpButtonClick(self, item):
        print(item)
        self.engine.pickUpItem(item)
 
    def makeScreen(self, screenDef, inventory):
        self.canvas = Canvas(self.engine.window, height = 500, width = 600)
        self.canvas.pack()
        self.title = Label(self.canvas, text = screenDef["title"])
        self.title.place(x = 1, y = 1)
        self.description = Label(self.canvas, text = screenDef['description'])
        self.description.place(x = 1, y = 20)
        self.northButton = Button(self.canvas, text = 'north', command = self.goNorth)
        self.eastButton = Button(self.canvas, text = 'east', command = self.goEast)
        self.southButton = Button(self.canvas, text = 'south', command = self.goSouth)
        self.westButton = Button(self.canvas, text = 'west', command = self.goWest)
        self.itemList = Listbox(self.canvas, selectmode = SINGLE)
        self.itemList.place(x = 230, y = 375, width = 100, height = 100)
        for item in inventory:
            self.itemList.insert(END, item)
        self.northButton.place(x = 50, y = 375)
        self.eastButton.place(x = 87, y = 412)
        self.southButton.place(x = 50, y = 450)
        self.westButton.place(x = 17, y = 412)
        toPickUp = lambda item = screenDef["items"][0]: self.onPickUpButtonClick(item)
        self.pickingUp = Button(self.canvas, text = 'pick up', command = toPickUp)
        self.pickingUp.place(x = 150, y = 375)
        if len(screenDef['items']) == 0:
            self.pickingUp.config(state = DISABLED)
            
        if not screenDef["directions"][NORTH]:
            self.northButton.config(state = DISABLED)

        if not screenDef["directions"][EAST]:
            self.eastButton.config(state = DISABLED)

        if not screenDef["directions"][SOUTH]:
            self.southButton.config(state = DISABLED)

        if not screenDef["directions"][WEST]:
            self.westButton.config(state = DISABLED)

    def updateScreen(self, screenDef, inventory):
            for item in inventory:
                self.itemList.insert(END, item)
            self.title.destroy()
            self.title = Label(self.canvas, text = screenDef["title"])
            self.title.place(x = 1, y = 1)
            self.description.destroy()
            self.description = Label(self.canvas, text = screenDef['description'])
            self.description.place(x = 1, y = 20)
            if len(screenDef['items']) == 0:
                self.pickingUp.config(state = DISABLED)
            else:
                self.pickingUp.config(state = 'normal')
            if screenDef["directions"][NORTH]:
                self.northButton.config(state = 'normal')

            else:
                self.northButton.config(state = DISABLED)

            if screenDef["directions"][EAST]:
                self.eastButton.config(state = 'normal')

            else:
                self.eastButton.config(state = DISABLED)

            if screenDef["directions"][SOUTH]:
                self.southButton.config(state = 'normal')

            else:
                self.southButton.config(state = DISABLED)

            if screenDef["directions"][WEST]:
                self.westButton.config(state = 'normal')

            else:
                self.westButton.config(state = DISABLED)
        
