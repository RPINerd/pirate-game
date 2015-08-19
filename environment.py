
from math import pi, sin, cos
from direct.task import Task
from direct.actor.Actor import Actor
from panda3d.core import Light, AmbientLight, DirectionalLight, Spotlight
from pandac.PandaModules import CompassEffect
from pandac.PandaModules import TransparencyAttrib
from panda3d.core import TextureStage
from direct.interval.LerpInterval import LerpTexOffsetInterval

 
class Sky():
    def __init__(self, base):
        self.timeOfDay = "morning"
        #self.skysphere = base.loader.loadModel('models/blue-sky-sphere')
        self.skysphere = base.loader.loadModel('models/farmsky')
        self.skysphere.setEffect(CompassEffect.make(base.render))
        self.skysphere.setScale(0.08)
        self.skysphere.reparentTo(base.render) 


class Water():
    def __init__(self, base):
        self.water = base.loader.loadModel('models/square.egg')
        self.water.setSx(base.worldsize*2)
        self.water.setSy(base.worldsize*2)
        self.water.setPos(base.worldsize/2,base.worldsize/2,25) # sea level
        #self.water.setPos(0,0,0)
        self.water.setTransparency(TransparencyAttrib.MAlpha) 
        newTS = TextureStage('1')
        self.water.setTexture(newTS,base.loader.loadTexture('models/water.png'))
        self.water.setTexScale(newTS,4)
        self.water.reparentTo(base.render)
        LerpTexOffsetInterval(self.water, 200, (1,0),(0,0), textureStage=newTS).loop()



