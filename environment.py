from direct.interval.LerpInterval import LerpTexOffsetInterval
from panda3d.core import AmbientLight, CompassEffect, DirectionalLight, TextureStage, TransparencyAttrib, Vec4


class Sky:
    def __init__(self, base):
        self.timeOfDay = "morning"
        # self.skysphere = base.loader.loadModel('models/blue-sky-sphere')
        self.skysphere = base.loader.loadModel("models/farmsky")
        self.skysphere.setEffect(CompassEffect.make(base.render))
        self.skysphere.setScale(1.0)
        self.skysphere.setPos(0.0, 0.0, -100.0)
        self.skysphere.reparentTo(base.render)
        self.initialize_lighting()

    def initialize_lighting(self):
        ambientLight_color = Vec4(0.5, 0.5, 0.5, 1)
        sunLight_color = Vec4(0.5, 0.5, 0.5, 1)
        backLight_color = Vec4(0.22, 0.44, 0.44, 1)
        if self.timeOfDay == "morning":
            ambientLight_color = Vec4(0.56, 0.52, 0.62, 1)
            sunLight_color = Vec4(0.86, 0.75, 0.63, 1)

        # Create Ambient Light
        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor(ambientLight_color)
        ambientLightNP = render.attachNewNode(ambientLight)
        render.setLight(ambientLightNP)

        # Create Directional Light
        sunLight = DirectionalLight("sunLight")
        sunLight.setColor(sunLight_color)
        sunLightNP = render.attachNewNode(sunLight)
        sunLightNP.setHpr(180, -20, 0)
        render.setLight(sunLightNP)

        # Create Directional Light
        backLight = DirectionalLight("backLight")
        backLight.setColor(backLight_color)
        backLightNP = render.attachNewNode(backLight)
        backLightNP.setHpr(-180, 160, 0)
        render.setLight(backLightNP)


class Water:
    def __init__(self, base):
        self.water = base.loader.loadModel("models/square.egg")
        self.water.setSx(base.worldsize * 2)
        self.water.setSy(base.worldsize * 2)
        self.water.setPos(base.worldsize / 2, base.worldsize / 2, 25)  # sea level
        # self.water.setPos(0,0,0)
        self.water.setTransparency(TransparencyAttrib.MAlpha)
        newTS = TextureStage("1")
        self.water.setTexture(newTS, base.loader.loadTexture("models/water.png"))
        self.water.setTexScale(newTS, 4)
        self.water.reparentTo(base.render)
        LerpTexOffsetInterval(self.water, 200, (1, 0), (0, 0), textureStage=newTS).loop()
