from Tkinter import *
from GameScreen import *
from World import *
from Player import *
from Enemy import *
from NavigationController import *
from InteractionController import *

class Engine:
    def __init__(self):
        self.window = Tk()
        self.window.title('Adventure Game')
        self.window.geometry('600x500')
        self.world = World(self)
        self.player = Player(self)
        self.enemy = Enemy(self)
        self.navigationController = NavigationController(self, self.world, self.player)
        self.interactionController = InteractionController(self, self.world, self.player, self.navigationController)
        self.gameScreen = GameScreen(self, self.navigationController, self.interactionController)

    def start(self):      
        self.gameScreen.makeScreen(self.world.worldDef[self.world.xCoordinate][self.world.yCoordinate], self.player.currentHP, self.player.maximalHP)
        self.gameScreen.updateScreen(self.world.worldDef[self.world.xCoordinate][self.world.yCoordinate], self.player.inventory, self.player.currentHP, self.player.maximalHP)
        self.window.mainloop()

    
    def giveSummary(self, direction):
        return self.world.giveSummary(direction)
        
game = Engine()
game.start()