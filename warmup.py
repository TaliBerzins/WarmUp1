from direct.showbase.ShowBase import ShowBase
import math, sys, random



class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.fighter = self.loader.loadModel('./Assets/sphere')
        self.fighter.reparentTo(self.render)
        self.fighter.setColorScale(1.0,0.0,0.0,1.0)

        self.accept('escape', self.quit)
        self.accept('arrow_left', self.negativeX, [1])
        self.accept('arrow_left-up', self.negativeX, [0])
        self.base = self

        self.base.disableMouse()

        self.base.camera.setPos(0.0, 0.0, 250.0)
        self.base.camera.setHpr(0.0, -90.0, 0.0)







        self.parent = self.loader.loadModel("./Assets/cube")

        x=0

        for i in range(100): 
            theta = x
            self.placeholder2 = self.render.attachNewNode('Placeholder2')
            self.placeholder2.setPos(50.0* math.cos(theta), 50.0 *math.sin(theta), 0.0 * math.tan(theta))
            red = 0.6 + random.random() * 0.4
            green = 0.6 + random.random() *0.4
            blue = 0.6 + random.random() * 0.4
            self.placeholder2.setColorScale(red, green, blue, 1.0)
            self.parent.instanceTo(self.placeholder2)
            x = x + 0.6

    def quit(self):
        sys.exit()

    def moveNegativeX(self, task):
        self.fighter.setX(self.fighter, -1)
        return task.cont # Sets the task to continue the next. game cycle

    def negativeX(self, keyDown):
        if(keyDown):
            self.taskMgr.add(self.moveNegativeX, 'moveNegativeX')
        else:
            self.taskMgr.remove('moveNegativeX')

            





     


app = MyApp()
app.run()