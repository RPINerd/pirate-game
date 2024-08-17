from direct.actor.Actor import Actor
from direct.task import Task
from panda3d.core import Vec3


class Ship:

    def __init__(self, base):
        self.base = base
        self.shipActor = Actor("models/panda-model")
        self.shipActor.setScale(0.05, 0.05, 0.05)
        self.shipActor.setPos(0.0, 0.0, 18.0)
        self.shipActor.reparentTo(self.base.render)
        self.set_camera_to_follow()

        self.keys = [0, 0, 0, 0, 0]
        self.initialize_controls()

    def initialize_controls(self):
        self.base.taskMgr.add(self.control_ship, "ship-control-task")
        self.base.accept("arrow_left", self.setKeys, [0, 1])
        self.base.accept("arrow_left-up", self.setKeys, [0, 0])
        self.base.accept("arrow_right", self.setKeys, [1, 1])
        self.base.accept("arrow_right-up", self.setKeys, [1, 0])
        self.base.accept("arrow_up", self.setKeys, [2, 1])
        self.base.accept("arrow_up-up", self.setKeys, [2, 0])

    def set_camera_to_follow(self):
        self.base.disableMouse()
        self.camera_offset = Vec3(50.0, 50.0, 30.0) * 5
        self.base.cam.setPos(self.shipActor.getPos() + self.camera_offset)
        self.base.cam.lookAt(self.shipActor.getPos())

    # switch upon which buttons are pressed with if statements
    def setKeys(self, btn, value):
        self.keys[btn] = value

    def control_ship(self, task):
        if self.keys[0]:
            self.shipActor.setHpr(self.shipActor.getHpr() + Vec3(1.0, 0.0, 0.0))

        if self.keys[1]:
            self.shipActor.setHpr(self.shipActor.getHpr() - Vec3(1.0, 0.0, 0.0))

        if self.keys[2]:
            forward_vector = self.shipActor.getMat().getRow3(1) * 5
            self.shipActor.setPos(self.shipActor.getPos() - forward_vector)
            self.base.cam.setPos(self.shipActor.getPos() + self.camera_offset)

        return Task.cont
