from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from world import World
from environment import Water, Sky
from ship import Ship

class PirateGame(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.worldsize = 1024
        self.camLens.setFov(60)
        game_world = World(self)

       

app = PirateGame()
app.run()