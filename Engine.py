from tkinter import *
from GameScreen import *

class Engine:
    def __init__(self):
        self.window = Tk()
        self.window.title('Adventure Game')
        self.window.geometry('600x500')
        self.gameScreen = GameScreen(self)

    def start(self):
        self.gameScreen.makeScreen()

game = Engine()
game.start()
