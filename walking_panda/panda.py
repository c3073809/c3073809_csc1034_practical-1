from math import pi, sin, cos
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from panda3d.core import AmbientLight, DirectionalLight, Vec4

class WalkingPanda(ShowBase):
    def __init__(self, no_rotate=False, scale=1, night_mode=False, panda_color='normal'):
        ShowBase.__init__(self)

        self.scene = self.loader.loadModel("models/environment")
        self.scene.reparentTo(self.render)
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        if night_mode:
            self.set_night_mode()
        else:
            self.set_day_mode()

        print(no_rotate)
        print(scale)
        print(night_mode)
        print(panda_color)

        if no_rotate == False:
            self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
        else:
            self.disableMouse()
            self.camera.setPos(0, -20, 3)

        #sound acquired from www.zapsplat.com
        mySound = self.loader.loadSfx("walking_panda/Jungle1.mp3")
        mySound.play()

        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})

        self.set_panda_color(panda_color)

        if scale ==1:
            self.pandaActor.setScale(0.001, 0.001, 0.001)
        else:
            self.pandaActor.setScale(0.005, 0.005, 0.005)
        self.pandaActor.reparentTo(self.render)

        self.pandaActor.loop("walk")

    def set_panda_color(self, panda_color):
        if panda_color == 'brown':
            self.pandaActor.setColorScale(0.65, 0.32, 0.18, 1)
        elif panda_color == 'black':
            self.pandaActor.setColorScale(0.1, 0.1, 0.1, 1)
        else:
            self.pandaActor.setColorScale(1, 1, 1, 1 )

    def set_day_mode(self):
        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor(Vec4(1, 1, 1, 1))
        ambientNP = self.render.attachNewNode(ambientLight)
        self.render.setLight(ambientNP)

        directionalLight = DirectionalLight("directionalLight")
        directionalLight.setColor(Vec4(1, 1, 0.9, 1))
        directionalNP = self.render.attachNewNode(directionalLight)
        directionalNP.setHpr(0, -60, 0)
        self.render.setLight(directionalNP)

        self.scene.clearColorScale()


    def set_night_mode(self):
        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor(Vec4(0.1, 0.1, 0.2, 1))
        ambientNP = self.render.attachNewNode(ambientLight)
        self.render.setLight(ambientNP)

        directionalLight = DirectionalLight("directionalLight")
        directionalLight.setColor(Vec4(0.2, 0.2, 0.5, 1))
        directionalNP = self.render.attachNewNode(directionalLight)
        directionalNP.setHpr(0, -60, 0)
        self.render.setLight(directionalNP)

        self.scene.setColorScale(0.2, 0.2, 0.4, 1)

    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont


