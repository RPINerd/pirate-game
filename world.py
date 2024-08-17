from panda3d.core import AmbientLight, Vec4

from environment import Sky, Water


class World:
    def __init__(self, base):
        self.objects = []
        self.base = base
        self.add_sky()
        self.add_water()
        self.add_ship()
        self.initialize_lighting()

    def add_sky(self):
        print("Here's the sky!")
        Sky(self.base)
        return "Sky"

    def add_water(self):
        Water(self.base)
        return "Water"

    def add_ship(self):
        return "Ship"

    def initialize_lighting(self):
        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor(Vec4(0.6, 0.6, 0.6, 1))
        self.base.render.setLight(self.base.render.attachNewNode(ambientLight))
