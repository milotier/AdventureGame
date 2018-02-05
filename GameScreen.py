from Tkinter import *
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
        self.engine.pickUpItem(item)

    def onDropButtonClick(self, item):
        self.engine.dropItem(item)
 
    def onScreenItemsSelect(self, evt):
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        self.pickingUp.config(state='normal')

    def onItemListSelect(self, evt):
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        self.drop.config(state='normal')

    def makeScreen(self, screenDef):
        self.canvas = Canvas(self.engine.window, height = 500, width = 600)
        self.canvas.pack()

        self.title = Label(self.canvas, text = screenDef["title"], font = 'Calibri 13 bold')
        self.title.place(x = 1, y = 1)

        self.description = Label(self.canvas, text = screenDef['description'])
        self.description.place(x = 1, y = 20)

        self.northButton = Button(self.canvas, text = 'north', command = self.goNorth)
        self.eastButton = Button(self.canvas, text = 'east', command = self.goEast)
        self.southButton = Button(self.canvas, text = 'south', command = self.goSouth)
        self.westButton = Button(self.canvas, text = 'west', command = self.goWest)
        self.northButton.place(x = 50, y = 375)
        self.eastButton.place(x = 87, y = 412)
        self.southButton.place(x = 50, y = 450)
        self.westButton.place(x = 17, y = 412)

        toPickUp = lambda : self.onPickUpButtonClick(self.screenItems.curselection())
        toDrop = lambda : self.onDropButtonClick(self.itemList.curselection())

        self.pickingUp = Button(self.canvas, text = 'pick up', command = toPickUp)
        self.pickingUp.place(x = 150, y = 375)
        self.drop = Button(self.canvas, text = 'drop', command = toDrop)
        self.drop.place(x = 150, y = 400)

        self.itemList = Listbox(self.canvas, selectmode = SINGLE)
        self.itemList.place(x = 230, y = 375, width = 100, height = 100)
        self.itemList.bind('<<ListboxSelect>>', self.onItemListSelect)
        self.inventoryLabel = Label(self.canvas, text = 'inventory:')
        self.inventoryLabel.place(x=240, y=350) 
     
        self.screenItems = Listbox(self.canvas, selectmode = SINGLE)
        self.screenItems.bind('<<ListboxSelect>>', self.onScreenItemsSelect)
        self.screenItems.place(x = 350, y = 375, width = 100, height = 100)
        self.screenItemsLabel = Label(self.canvas, text='visible items:')
        self.screenItemsLabel.place(x=355, y=350)              

    def updateScreen(self, screenDef, inventory):
        self.title.destroy()
        self.title = Label(self.canvas, text = screenDef["title"], font='Calibri 13 bold')
        self.title.place(x = 1, y = 1)

        self.description.destroy()
        self.description = Label(self.canvas, text = screenDef['description'])
        self.description.place(x = 1, y = 20)

        toPickUp = lambda : self.onPickUpButtonClick(self.screenItems.curselection())
        toDrop = lambda : self.onDropButtonClick(self.itemList.curselection())
        self.pickingUp.config(command=toPickUp)
        self.drop.config(command=toDrop)
        self.pickingUp.config(state = DISABLED)
        self.drop.config(state=DISABLED)

        self.itemList.delete(0, END)
        for item in inventory:
            self.itemList.insert(END, item)
            
        self.screenItems.delete(0, END)
        for item in screenDef['items']:
            self.screenItems.insert(END, item)

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
        
