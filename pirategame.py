from direct.showbase.ShowBase import ShowBase

from ship import Ship
from world import World


class PirateGame(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.worldsize = 1024
        self.camLens.setFov(60)
        World(self)
        Ship(self)


app = PirateGame()
app.run()
