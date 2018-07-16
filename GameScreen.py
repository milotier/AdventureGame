from Tkinter import *
from World import *
from NavigationController import *

class GameScreen:
    def __init__(self, engine, navigationController, interactionContoller):
        self.engine = engine
        self.navigationController = navigationController
        self.navigationController.setGameScreen(self)
        self.interactionContoller = interactionContoller
        self.interactionContoller.setGameScreen(self)

    def goNorth(self):
        self.navigationController.askNextRoom(NORTH)
    
    def goEast(self):
        self.navigationController.askNextRoom(EAST)

    def goSouth(self):
        self.navigationController.askNextRoom(SOUTH)

    def goWest(self):
        self.navigationController.askNextRoom(WEST)

    def onPickUpButtonClick(self, item):        
        self.interactionContoller.pickUpItem(item)

    def onDropButtonClick(self, item):
        self.interactionContoller.dropItem(item)

    def onUseButtonClick(self, item):
        self.interactionContoller.useItem(item)
 
    def onScreenItemsSelect(self, evt):
        w = evt.widget
        self.pickingUp.config(state='normal')

    def onItemListSelect(self, evt):
        w = evt.widget
        self.drop.config(state='normal')
        self.use.config(state='normal')

    def onObstacleListSelect(self, w, item):
        index = int(w.curselection()[0])
        obstacleName = w.get(index)
        self.interactionContoller.removeObstacle(obstacleName, item)

    def destroyPopupmessage(self):
        self.obstacleList.destroy()
        self.obstacleLabel.destroy()
        self.cancelButton.destroy()
        
    def cantUseItem(self, reason):
        if reason == 'no obstacle':
            self.cantUse = Label(self.canvas, text='There\'s nothing to use that item on.')
            self.cantUse.place(x=175, y=200)
            self.engine.window.update()
            self.engine.window.after(3000, self.cantUse.destroy())
        if reason == 'wrong obstacle':
            self.cantUse = Label(self.canvas, text='You can\'t use that item on that obstacle.')
            self.cantUse.place(x=175, y=175)
            self.engine.window.update()
            self.engine.window.after(3000, self.cantUse.destroy())

    def askWhichObstacle(self, screenDef, item):
        self.obstacleLabel = Label(self.canvas, text='Where do you want to use it on?')
        self.obstacleLabel.place(x=175, y=150)
        self.obstacleList = Listbox(self.canvas, selectmode=SINGLE)
        for direction in screenDef['directions']:
            direction = screenDef['directions'].get(direction)
            if direction != None and 'name' in direction:
                name = direction['name']
                self.obstacleList.insert(END, name)
        self.obstacleList.place(x=225, y=200, width=120, height=100)
        self.cancelButton = Button(self.canvas, text='cancel', command=self.destroyPopupmessage)
        self.cancelButton.place(x=230, y=310)

        toObstacleListSelect = lambda (evt): self.onObstacleListSelect(evt.widget, item)

        self.obstacleList.bind('<<ListboxSelect>>', toObstacleListSelect)
        
    def makeScreen(self, screenDef, currentHP, maximalHP):
        self.canvas = Canvas(self.engine.window, height=500, width=600)
        self.canvas.pack()

        self.title = Label(self.canvas, text=screenDef["title"], font='Calibri 13 bold')
        self.title.place(x=1, y=1)

        self.hpLabel = Label(self.canvas, text = 'HP: ' + str(currentHP) + '/' + str(maximalHP))
        self.hpLabel.place(x=500, y=1)

        self.northButton = Button(self.canvas, text='north', command=self.goNorth)
        self.eastButton = Button(self.canvas, text='east', command=self.goEast)
        self.southButton = Button(self.canvas, text='south', command=self.goSouth)
        self.westButton = Button(self.canvas, text='west', command=self.goWest)
        self.northButton.place(x=50, y=375)
        self.eastButton.place(x=87, y=412)
        self.southButton.place(x=50, y=450)
        self.westButton.place(x=17, y=412)

        toPickUp = lambda : self.onPickUpButtonClick(self.screenItems.curselection())
        toDrop = lambda : self.onDropButtonClick(self.itemList.curselection())
        toUse = lambda : self.onUseButtonClick(self.itemList.curselection())
        self.pickingUp = Button(self.canvas, text='pick up', command=toPickUp)
        self.pickingUp.place(x=150, y=375)
        self.drop = Button(self.canvas, text='drop', command = toDrop)
        self.drop.place(x=150, y=400, width=74)

        self.use = Button(self.canvas, text='use', command = toUse)
        self.use.place (x=150, y=425, width=74)

        self.itemList = Listbox(self.canvas, selectmode=SINGLE)
        self.itemList.place(x=230, y=375, width=100, height=100)
        self.itemList.bind('<<ListboxSelect>>', self.onItemListSelect)
        self.inventoryLabel = Label(self.canvas, text='inventory:')
        self.inventoryLabel.place(x=240, y=350) 
     
        self.screenItems = Listbox(self.canvas, selectmode=SINGLE)
        self.screenItems.bind('<<ListboxSelect>>', self.onScreenItemsSelect)
        self.screenItems.place(x=350, y=375, width=100, height=100)
        self.screenItemsLabel = Label(self.canvas, text='visible items:')
        self.screenItemsLabel.place(x=355, y=350)              

    def updateScreen(self, screenDef, inventory, currentHP, maximalHP):
        self.title.destroy()
        self.title = Label(self.canvas, text=screenDef["title"], font='Calibri 13 bold')
        self.title.place(x = 1, y = 1)

        self.hpLabel = Label(self.canvas, text='HP: ' + str(currentHP) + '/' + str(maximalHP))
        self.hpLabel.place(x=500, y=1)

        toPickUp = lambda : self.onPickUpButtonClick(self.screenItems.curselection())
        toDrop = lambda : self.onDropButtonClick(self.itemList.curselection())
        toUse = lambda : self.onUseButtonClick(self.itemList.curselection())
        self.pickingUp.config(command=toPickUp)
        self.drop.config(command=toDrop)
        self.use.config(command=toUse)
        self.pickingUp.config(state = DISABLED)
        self.drop.config(state=DISABLED)
        self.use.config(state=DISABLED)

        self.itemList.delete(0, END)
        for item in inventory:
            self.itemList.insert(END, item)

        self.screenItems.delete(0, END)
        for item in screenDef['items']:
            self.screenItems.insert(END, item)

        summaryText = ""
        northDirection = screenDef['directions'].get(NORTH)
        eastDirection = screenDef['directions'].get(EAST)
        southDirection = screenDef['directions'].get(SOUTH)
        westDirection = screenDef['directions'].get(WEST)
        if NORTH in screenDef["directions"] and northDirection == None:
            self.northButton.config(state='normal')
            summaryText += "To the north you see " + self.engine.giveSummary(NORTH) + "\n"
        elif NORTH in screenDef["directions"]:
            summaryText += 'To the north you see ' + northDirection['name'] + '\n'
            self.northButton.config(state=DISABLED)
        else:
            self.northButton.config(state = DISABLED)

        if EAST in screenDef["directions"] and eastDirection == None:
            self.eastButton.config(state='normal')
            summaryText += 'To the east you see ' + self.engine.giveSummary(EAST) + '\n'
        elif EAST in screenDef["directions"]:
            summaryText += 'To the east you see ' + eastDirection['name'] + '\n'
            self.eastButton.config(state=DISABLED)
        else:
            self.eastButton.config(state=DISABLED)

        if SOUTH in screenDef["directions"] and southDirection == None:
            self.southButton.config(state = 'normal')
            summaryText += 'To the south you see ' + self.engine.giveSummary(SOUTH) + '\n'
        elif SOUTH in screenDef["directions"]:
            summaryText += 'To the south you see ' + southDirection['name'] + '\n'
            self.southButton.config(state=DISABLED)
        else:
            self.southButton.config(state=DISABLED)

        if WEST in screenDef["directions"] and westDirection == None:
            self.westButton.config(state='normal')
            summaryText +=  'To the west you see ' + self.engine.giveSummary(WEST) + '\n'
        elif WEST in screenDef["directions"]:
            summaryText += 'To the west you see ' + westDirection['name'] + '\n'
            self.westButton.config(state=DISABLED)
        else:
            self.westButton.config(state = DISABLED)
        
        description = screenDef['description'] + '\n' + summaryText

        self.description = Text(self.canvas, font='Calibri', width=50, height=5)
        self.description.insert(END, description)
        self.description.config(state=DISABLED)
        self.description.place( x=1, y=20)

