from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from environment import Water, Sky
from ship import Ship
from panda3d.core import AmbientLight, Vec4
 
class World():
    def __init__(self, base):
        self.objects = []
        self.add_sky()
        self.add_water()
        self.add_ship()
        self.base = base
        self.initialize_lighting()




    def add_sky(self):
        print "Here's the sky!"
        sky = Sky(base)
        return "Sky"



    def add_water(self): 
        water = Water(base)
        return "Water"
        
    def add_ship(self):
        return "Ship"

    def initialize_lighting(self):
        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor(Vec4(.6, .6, .6, 1))
        base.render.setLight(base.render.attachNewNode(ambientLight))
