from tkinter import *

class GameScreen:
    def __init__(self, engine):
        self.engine = engine

    def makeScreen(self):
        self.canvas = Canvas(self.engine.window, height = 500, width = 600)
        self.canvas.pack()
        Label(self.canvas, text = 'Test').pack()
    
        
