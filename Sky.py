
from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from panda3d.core import Light, AmbientLight, DirectionalLight, Spotlight

 
class Sky(ShowBase):
 
    def __init__(self):
        self.timeOfDay =

        self.initialize_lighting()

